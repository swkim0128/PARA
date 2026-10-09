"""당선인 정보 수집 스크립트.

중앙선관위 OpenAPI `WinnerInfoInqireService2/getWinnerInfoInqire` 호출.

응답 주요 필드: name, jdName, sggName, sdName, wiwName, dugsu, dugyul, addr, job, edu.

사용 예:
    python -m scripts.fetch_winners --sg-id 20260603 --sg-type 3
"""

from __future__ import annotations

import argparse
import time
from typing import Any

import pandas as pd

from scripts.common import (
    BASE_URL,
    PROJECT_ROOT,
    check_result,
    create_client,
    load_api_key,
    save_raw_json,
    with_retry,
)

ENDPOINT = f"{BASE_URL}/WinnerInfoInqireService2/getWinnerInfoInqire"


def parse_args() -> argparse.Namespace:
    """CLI 인자를 파싱한다."""
    parser = argparse.ArgumentParser(description="당선인 정보 수집")
    parser.add_argument("--sg-id", default="20260603", help="선거ID (YYYYMMDD 8자리)")
    parser.add_argument("--sg-type", required=True, help="선거종류코드")
    parser.add_argument("--sd-name", default=None, help="시도명 (선택)")
    parser.add_argument("--sgg-name", default=None, help="선거구명 (선택)")
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
    sd_name: str | None,
    sgg_name: str | None,
) -> dict:
    """단일 페이지 호출."""
    params: dict[str, Any] = {
        "ServiceKey": service_key,
        "pageNo": page_no,
        "numOfRows": page_size,
        "resultType": result_type,
        "sgId": sg_id,
        "sgTypecode": sg_type,
    }
    if sd_name:
        params["sdName"] = sd_name
    if sgg_name:
        params["sggName"] = sgg_name

    response = client.get(ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def extract_items(payload: dict) -> list[dict]:
    """응답의 items 리스트를 정규화하여 반환."""
    body = payload.get("response", {}).get("body", {})
    items = body.get("items", [])
    if isinstance(items, dict):
        items = items.get("item", [])
    if isinstance(items, dict):
        items = [items]
    return items or []


def extract_total_count(payload: dict) -> int:
    """totalCount 를 정수로 추출."""
    body = payload.get("response", {}).get("body", {})
    try:
        return int(body.get("totalCount", 0))
    except (TypeError, ValueError):
        return 0


def main() -> None:
    """전체 페이지를 순회 수집하고 parquet 로 저장한다."""
    args = parse_args()
    service_key = load_api_key()
    sd_tag = args.sd_name or "ALL"

    all_items: list[dict] = []
    with create_client() as client:
        page_no = 1
        total_count = None
        while True:
            payload = fetch_page(
                client=client,
                service_key=service_key,
                sg_id=args.sg_id,
                sg_type=args.sg_type,
                page_no=page_no,
                page_size=args.page_size,
                result_type=args.result_type,
                sd_name=args.sd_name,
                sgg_name=args.sgg_name,
            )
            raw_name = f"winners_sg{args.sg_type}_{sd_tag}_p{page_no}"
            raw_path = save_raw_json(payload, raw_name)
            check_result(payload, raw_path)

            items = extract_items(payload)
            all_items.extend(items)

            if total_count is None:
                total_count = extract_total_count(payload)
                print(f"[info] totalCount={total_count}")

            fetched = page_no * args.page_size
            print(
                f"[info] page={page_no} items={len(items)} "
                f"cumulative={len(all_items)} raw={raw_path}"
            )
            if fetched >= total_count or not items:
                break
            page_no += 1
            time.sleep(0.5)

    if not all_items:
        print("[warn] 수집된 항목이 없습니다. parquet 저장을 건너뜁니다.")
        return

    df = pd.DataFrame(all_items)
    parsed_dir = PROJECT_ROOT / "data" / "parsed"
    parsed_dir.mkdir(parents=True, exist_ok=True)
    out_path = parsed_dir / f"winners_sg{args.sg_type}.parquet"
    df.to_parquet(out_path, index=False)
    print(f"[done] {len(df)} rows -> {out_path}")


if __name__ == "__main__":
    main()
