"""중앙선관위 OpenAPI 호출용 공용 헬퍼.

- API 키 로딩 (dotenv 기반, 디코딩 키 우선)
- httpx 클라이언트 생성 팩토리
- tenacity 기반 재시도 데코레이터
- 응답 결과코드 검증
- 원본 JSON 저장
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Final

import httpx
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

# 공공데이터포털 중앙선관위 베이스 URL (https 필수)
BASE_URL: Final[str] = "https://apis.data.go.kr/9760000"

# 프로젝트 루트 (scripts/ 의 부모)
PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent


def load_api_key() -> str:
    """환경변수에서 API 키를 로드한다.

    `NEC_API_KEY_DECODED`(일반 인증키, Decoding) 가 우선이며,
    없을 경우 `NEC_API_KEY_ENCODED`(Encoding) 를 반환한다.
    둘 다 없으면 RuntimeError 를 raise 한다.

    Returns:
        str: API 키 문자열.

    Raises:
        RuntimeError: 두 환경변수 모두 비어 있을 때.
    """
    load_dotenv(PROJECT_ROOT / ".env")
    decoded = os.getenv("NEC_API_KEY_DECODED")
    encoded = os.getenv("NEC_API_KEY_ENCODED")
    if decoded:
        return decoded
    if encoded:
        return encoded
    raise RuntimeError(
        "API 키가 설정되지 않았습니다. "
        ".env 파일에 NEC_API_KEY_DECODED 또는 NEC_API_KEY_ENCODED 를 정의하세요. "
        "(샘플은 .env.example 참고)"
    )


def create_client(timeout: float = 30.0) -> httpx.Client:
    """기본 timeout 을 지정한 httpx.Client 를 생성한다.

    Args:
        timeout: 초 단위 타임아웃. 기본 30초.

    Returns:
        httpx.Client: 호출 측에서 with 구문으로 close 할 것.
    """
    return httpx.Client(timeout=timeout)


# tenacity 재시도 데코레이터: 네트워크/응답코드 양쪽 모두 대상.
with_retry = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=10),
    retry=lambda retry_state: isinstance(
        retry_state.outcome.exception(), (httpx.HTTPError, RuntimeError)
    )
    if retry_state.outcome is not None and retry_state.outcome.failed
    else False,
    reraise=True,
)


def check_result(payload: dict, raw_path: Path) -> dict:
    """OpenAPI 응답의 resultCode 가 '00' 인지 검증한다.

    실패 시 원본 JSON 은 이미 저장된 상태로 유지하고 RuntimeError 를 raise 한다.

    Args:
        payload: API 응답 dict.
        raw_path: 원본 JSON 이 저장된 경로 (오류 메시지에 노출).

    Returns:
        dict: 정상 응답이면 payload 를 그대로 반환.

    Raises:
        RuntimeError: resultCode 가 '00' 이 아닐 때.
    """
    try:
        header = payload["response"]["header"]
    except (KeyError, TypeError) as exc:
        raise RuntimeError(
            f"응답 구조가 예상과 다릅니다 (response.header 없음). "
            f"raw_path={raw_path}, error={exc!r}"
        ) from exc

    result_code = header.get("resultCode")
    result_msg = header.get("resultMsg", "")
    if result_code != "00":
        raise RuntimeError(
            f"API 응답 오류: resultCode={result_code}, "
            f"resultMsg={result_msg}, raw_path={raw_path}"
        )
    return payload


def save_raw_json(payload: dict, name: str) -> Path:
    """원본 JSON 응답을 data/raw/{YYYY-MM-DD}/{name}.json 에 저장한다.

    Args:
        payload: 저장할 응답 dict.
        name: 파일명 (확장자 제외).

    Returns:
        Path: 저장된 파일의 절대 경로.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    raw_dir = PROJECT_ROOT / "data" / "raw" / today
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / f"{name}.json"
    with path.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, ensure_ascii=False, indent=2)
    return path


if __name__ == "__main__":
    # 키 로드 동작 확인 (전체 키는 절대 출력하지 않음)
    key = load_api_key()
    print(f"{key[:8]}... (length={len(key)})")
