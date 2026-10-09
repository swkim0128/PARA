# Election-2026-Local-Archive

## 1. 프로젝트 목적

제9회 전국동시지방선거(2026년 6월 3일) 관련 **중앙선거관리위원회 공식 데이터**를 1차 자료 형태로 아카이빙하는 프로젝트입니다.

- **목적은 분석이 아닌 보존**입니다. 시간이 지나면 사라지거나 변경될 수 있는 원천 데이터를 시점 스냅샷 형태로 저장합니다.
- **부정선거 가설의 입증/반증 어느 쪽도 선험적으로 전제하지 않습니다.** 결론이 아닌 자료의 무결성·재현성에 집중합니다.
- 누구든 동일 절차로 동일 데이터를 다시 받아볼 수 있도록 스크립트와 호출 파라미터를 기록합니다.

## 2. 데이터 소스

- **data.go.kr 공공데이터포털 OpenAPI 4종** (주력)
  - `VoteXmntckInfoInqireService2` — 투·개표 정보
  - `WinnerInfoInqireService2` — 당선인 정보
  - `CountingSttnInfoInqireService` — 개표소 정보
  - 코드 정보 조회 서비스 (선거종류·정당·지역 코드)
- **data.nec.go.kr** 일괄 파일 다운로드 (옵션, 추후 확장)
- info.nec.go.kr 직접 크롤링은 사용하지 않습니다 (아래 §3 참조).

## 3. 법적·윤리적 고려

- **info.nec.go.kr 직접 크롤링은 robots.txt를 위반하므로 금지합니다.** 본 프로젝트는 오로지 공공데이터포털 공식 OpenAPI만 사용합니다.
- data.go.kr 활용신청을 통해 발급받은 인증키를 사용합니다.
- 개발계정 트래픽 한도는 **10,000건/일** 입니다. 페이지네이션·정렬을 신중히 구성하여 한도를 넘기지 않도록 합니다.
- **개인정보(주민등록번호·전화번호·이메일 등)는 수집·저장하지 않습니다.** 당선인 응답에 포함되는 주소·학력 등은 공개 정보이지만, 보관 시 가능하면 익명화·축약(예: 시군 단위까지만) 처리합니다.
- 본 저장소에는 인증키, 원시 응답 데이터, 가공된 데이터셋(`data/raw/`, `data/parsed/*.parquet`, `data/parsed/*.csv`)을 커밋하지 않습니다 (`.gitignore` 참조).

## 4. 재현 절차

```bash
# 1) 의존성 격리 (권장)
python -m venv .venv
source .venv/bin/activate

# 2) 의존성 설치
pip install -r requirements.txt

# 3) 환경 변수 준비
cp .env.example .env
# .env 를 열어 NEC_API_KEY_ENCODED / NEC_API_KEY_DECODED 둘 중 하나 이상을 채운다.

# 4) 수집 스크립트 실행 (예시 — sgTypecode=3 시·도지사)
python -m scripts.fetch_vote_results --sg-type 3
python -m scripts.fetch_winners --sg-type 3
python -m scripts.fetch_counting_stations --sg-type 3
```

원시 응답은 `data/raw/{YYYY-MM-DD}/...json`, 가공본은 `data/parsed/*.parquet`에 저장됩니다.

## 5. 데이터 사전 (스키마)

각 API 응답 필드 명세는 [`docs/schema.md`](docs/schema.md) 참조.

## 6. 선거종류코드(sgTypecode) 매핑

- 첫 호출 결과로 채워나가는 living document 입니다.
- 현재 매핑은 [`docs/election_type_codes.md`](docs/election_type_codes.md) 참조.

## 7. 변경 이력

<!-- 빈 섹션 — 작업 진행 시 날짜별로 추가 -->
