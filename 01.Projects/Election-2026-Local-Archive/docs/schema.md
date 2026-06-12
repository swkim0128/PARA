# OpenAPI 응답 스키마

## 1. 투·개표 정보 (`getVoteSttusInfoInqire`)

| 항목명(국문) | 영문 | 크기 | 필수 | 샘플 |
|---|---|---|---|---|
| 결과코드 | resultCode | 2 | 필수 | 00 |
| 결과메시지 | resultMsg | 50 | 필수 | OK |
| 한 페이지 결과 수 | numOfRows | 4 | 필수 | 10 |
| 페이지 번호 | pageNo | 4 | 필수 | 1 |
| 전체 결과 수 | totalCount | 4 | 필수 | 3 |
| 선거ID | sgId | 10 | 필수 | 20260603 |
| 선거종류코드 | sgTypecode | 2 | 필수 | 3 |
| 시도명 | sdName | 40 | 필수 | 서울특별시 |
| 구시군명 | wiwName | 40 | 옵션 | 강서구 |
| 총선거인수 | totSunsu | 10 | 옵션 | 1000 |
| 선거일투표 선거인수 | psSunsu | 10 | 옵션 | 900 |
| 거소·사전·선상·재외 선거인수 | psEtcSunsu | 10 | 옵션 | 200 |
| 총 투표자수 | totTusu | 10 | 옵션 | 800 |
| 선거일 투표자수 | psTusu | 10 | 옵션 | 700 |
| 거소·사전·선상·재외 투표자수 | psEtcTusu | 10 | 옵션 | 100 |
| 투표율 | Turnout | 10 | 옵션 | 80 |
| 정렬순서 | vrOrder | 3 | 옵션 | 1 |
| 결과순서 | num | 8 | 필수 | 1 |

⚠️ **이 API는 후보별 득표가 아닌 시도/구시군 단위 투표 통계만 반환한다.** 후보별 득표는 당선인 API 또는 data.nec.go.kr 파일 다운로드 경로를 사용해야 한다.

## 2. 당선인 정보 (`getWinnerInfoInqire`)

| 항목명 | 영문 | 크기 | 필수 | 샘플 |
|---|---|---|---|---|
| 결과코드 | resultCode | 2 | 필수 | 00 |
| 결과메시지 | resultMsg | 50 | 필수 | OK |
| 한 페이지 결과 수 | numOfRows | 4 | 필수 | 10 |
| 페이지 번호 | pageNo | 4 | 필수 | 1 |
| 전체 결과 수 | totalCount | 4 | 필수 | 3 |
| 선거ID | sgId | 10 | 필수 | 20260603 |
| 선거종류코드 | sgTypecode | 2 | 필수 | 3 |
| 한글성명 | name | 50 | 옵션 | 홍길동 |
| 정당명 | jdName | 50 | 옵션 | OO당 |
| 선거구명 | sggName | 50 | 옵션 | 전주시을 |
| 시도명 | sdName | 40 | 옵션 | 전라북도 |
| 구시군명 | wiwName | 40 | 옵션 | 전주시완산구 |
| 득표수 | dugsu | 10 | 옵션 | 100 |
| 득표율 | dugyul | 10 | 옵션 | 100 |
| 주소 | addr | 200 | 옵션 | 전라북도 전주시 완산구 청운효자동 |
| 직업 | job | 200 | 옵션 | 정치인 |
| 학력 | edu | 200 | 옵션 | 대졸 |

## 3. 개표소 정보 (`CountingSttnInfoInqireService`)
첫 호출 후 응답을 보고 채워 넣을 예정 (living document).
