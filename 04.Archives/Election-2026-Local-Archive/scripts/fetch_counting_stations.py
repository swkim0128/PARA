"""개표소 정보 수집 스크립트 (탐색 단계).

중앙선관위 OpenAPI `CountingSttnInfoInqireService` 시리즈 호출.

⚠️ 정확한 subpath 는 data.go.kr 상세 페이지에서 확인 필요.
    기본값으로 `getCountingSttnInfoInqire` 를 가정한다.

사용 예:
    python -m scripts.fetch_counting_stations --sg-id 20260603 --sg-type 3
"""

from __future__ import annotations

import argparse
from typing import Any

from scripts.common import (
    BASE_URL,
    check_result,
    create_client,
    load_api_key,
    save_raw_json,
    with_retry,
)

# 정확한 subpath 는 data.go.kr 상세 페이지에서 확인 후 갱신 필요.
SUBPATH = "getCountingSttnInfoInqire"
ENDPOINT = f"{BASE_URL}/CountingSttnInfoInqireService/{SUBPATH}"


def parse_args() -> argparse.Namespace:
    """CLI 인자를 파싱한다."""
    parser = argparse.ArgumentParser(description="개표소 정보 탐색 호출")
    parser.add_argument("--sg-id", default="20260603", help="선거ID (YYYYMMDD)")
    parser.add_argument("--sg-type", required=True, help="선거종류코드")
    parser.add_argument("--page-size", type=int, default=100, help="numOfRows")
    parser.add_argument("--result-type", default="json", help="응답 포맷")
    return parser.parse_args()


@with_retry
def fetch_page(
    client: Any,
    service_key: str,
    sg_id: str,
    sg_type: str,
    page_no: int,
    page_size: int,
    result_type: str,
) -> dict:
    """단일 페이지 호출. 최소 파라미터(sgId, sgTypecode) 만 우선 시도한다."""
    params: dict[str, Any] = {
        "ServiceKey": service_key,
        "pageNo": page_no,
        "numOfRows": page_size,
        "resultType": result_type,
        "sgId": sg_id,
        "sgTypecode": sg_type,
    }
    response = client.get(ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """첫 페이지만 호출하여 응답 구조를 확인하기 위한 탐색용 진입점."""
    args = parse_args()
    service_key = load_api_key()
    with create_client() as client:
        payload = fetch_page(
            client=client,
            service_key=service_key,
            sg_id=args.sg_id,
            sg_type=args.sg_type,
            page_no=1,
            page_size=args.page_size,
            result_type=args.result_type,
        )
        raw_path = save_raw_json(payload, f"counting_stations_sg{args.sg_type}_p1")
        check_result(payload, raw_path)
        print(f"[ok] raw saved: {raw_path}")
        print(
            "[next] 응답 구조를 확인한 뒤 docs/schema.md 의 "
            "'3. 개표소 정보' 섹션에 필드 표를 기록하세요. "
            "subpath 가 다르면 SUBPATH 상수를 갱신하세요."
        )


if __name__ == "__main__":
    main()
