# WIKI.md — LLM Wiki 운영 스키마

> 이 파일은 **LLM이 위키를 유지·갱신할 때 따르는 규칙의 단일 진실의 원천(SoT)**이다. Karpathy의 "LLM Wiki" 아이디어를 PARA 볼트에 적용한 구성.

## 1. 3-Layer 아키텍처

| Layer | 위치 | 누가 소유 |
|---|---|---|
| **Raw Sources** (불변) | `03.Resources/Wiki/_Sources/` (수집 후), `01~04.{PARA}/` (PARA 컨텍스트 자료) | 사용자 (수집·큐레이션) |
| **Wiki** (LLM 소유) | `03.Resources/Wiki/{Entities,Concepts,Topics,Comparisons}/`, `index.md`, `log.md` | LLM (생성·갱신·교차참조) |
| **Schema** (이 파일) | `03.Resources/Wiki/WIKI.md` | 사용자 (규칙 정의) |

**불변 규칙**: LLM은 `_Sources/` 안의 원천 파일을 **절대 수정하지 않는다**. 합성/요약은 별도 위키 페이지에 작성하고 원천은 링크만 한다.

## 2. PARA 정합

위키는 PARA `03.Resources/` 하위(`03.Resources/Wiki/`)에 위치하며, PARA 폴더(01~04)의 다른 자료와 **공존**한다. 두 가지 룰로 정합:

1. **소유권**: 원천 자료(논문·기사·노트·강의)는 의미에 맞게 PARA 또는 `03.Resources/Wiki/_Sources/` 어디든 둘 수 있음. 위키 페이지(엔티티·개념 등)는 무조건 `03.Resources/Wiki/` 하위.
2. **PARA 라벨링**: 모든 위키 페이지 frontmatter에 `para:` 필드로 1차 컨텍스트 명시. `[[wikilink]]`로 PARA 항목과 양방향 연결.

| `para:` 값 | 의미 |
|---|---|
| `project` | 특정 프로젝트(`01.Projects/X/`)와 직접 연관 |
| `area` | 영역 책임(`02.Areas/X/`)에 속함 |
| `resource` | 일반 참고자료(`03.Resources/`) |
| `archive` | 비활성 (`04.Archives/`) |
| `wiki` | 위키 내부 합성만 (PARA 외) |

## 3. 페이지 타입

| 타입 | 폴더 | 용도 |
|---|---|---|
| **Source** | `_Sources/{articles,notes,chats}/` | 원천 자료의 요약·메타 (원본 본문은 첨부 또는 링크) |
| **Entity** | `Entities/` | 인물·제품·조직·도구 등 고유 명사 |
| **Concept** | `Concepts/` | 아이디어·패턴·이론·기법 |
| **Topic** | `Topics/` | 광범위한 주제 (여러 Concept·Entity 묶음) |
| **Comparison** | `Comparisons/` | X vs Y 같은 합성 분석 |

## 4. Frontmatter 표준

모든 위키 페이지 상단에 YAML frontmatter:

```yaml
---
type: source | entity | concept | topic | comparison
para: project | area | resource | archive | wiki
para_link: "[[01.Projects/X]]"   # 선택, 구체적 PARA 항목 wikilink
status: active | stable | stale | superseded
sources: ["[[_Sources/article-x]]", ...]
related: ["[[Entity-Y]]", "[[Concept-Z]]", ...]
tags: [tag1, tag2]
created: 2026-06-03
updated: 2026-06-03
---
```

- `status` 의미:
  - `active`: 최근 활발히 갱신
  - `stable`: 안정 상태
  - `stale`: 1개월+ 미갱신, lint 시 점검
  - `superseded`: 다른 페이지로 대체됨 (링크 추가 후 보존)

## 5. 명명 규칙

- 파일명: 한국어 자유, 공백 OK (예: `법안 git graph.md`)
- 엔티티 페이지명: 그대로 이름 (예: `Karpathy.md`)
- 개념 페이지명: 의미 단위 (예: `Saga 패턴.md`)
- 비교 페이지명: `X vs Y.md`
- 소스 페이지명: `YYYY-MM-DD - title.md` (날짜 prefix로 시간 정합)

## 6. 핵심 파일

### `index.md` — 내용 인덱스
LLM이 **매 ingest마다** 갱신. 카테고리별 분류 + 1줄 요약 + 선택 메타. 100+ 페이지 규모에서 LLM이 관련 페이지를 찾는 진입점.

### `log.md` — 연대순 로그
**append-only**. 매 ingest/query-as-page/lint 후 항목 추가:
```
## [YYYY-MM-DD] ingest | Source title (source-page)
- Created: [[Entity-A]], [[Concept-B]]
- Updated: [[Topic-C]], [[Entity-D]]
- Notes: ...
```

## 7. 워크플로

### Ingest
1. 사용자: `_Inbox/` 에 원천 파일 두기 (직접 또는 `scripts/wiki_new_source.sh` 사용)
2. 사용자: Claude에 `"인박스 X 수집해줘"` 요청 → `prompts/ingest.md` 자동 적용
3. LLM:
   - 원천 읽기
   - `_Sources/{articles|notes|chats}/` 에 Source 페이지 생성 (원본은 `Inbox`에서 이동 또는 링크)
   - 엔티티·개념 추출 → 기존 페이지 갱신 또는 신규 생성 (10-15개 페이지 영향 정상)
   - 교차 참조 wikilinks 갱신
   - `index.md` 갱신
   - `log.md` 항목 추가
4. 사용자: Obsidian Graph View로 결과 확인

### Query
1. 사용자: Claude에 질문 → `prompts/query.md` 적용
2. LLM:
   - `03.Resources/Wiki/` 검색 (index 우선 → 관련 페이지 drill-down)
   - 인용 포함 답변
   - **가치 있는 답변은 새 페이지로 파일링 제안** (사용자 승인 시 페이지 생성)

### Lint
주기: 사용자 요청 시 (권장: 주 1회 또는 50 ingest마다).
1. 사용자: `"위키 lint 돌려줘"`
2. LLM: `prompts/lint.md` 적용 →
   - **Orphans**: inbound link 0인 페이지
   - **Stale**: `status=stale` 또는 30+일 미갱신
   - **Contradictions**: 같은 엔티티에 모순된 사실
   - **Missing concepts**: 자주 언급되나 페이지 없는 항목
   - **Data gaps**: 핵심 필드 비어있는 페이지
3. 리포트 출력 + 사용자 승인 시 자동 수정

## 8. 사용자-LLM 역할 분담

| 사용자 | LLM |
|---|---|
| 원천 큐레이션 (어떤 글을 읽을지) | 원천 읽기·요약 |
| 질문·분석 방향 결정 | 페이지 생성·갱신·링크 |
| 의미·맥락 판단 | 교차 참조 유지·중복 정합 |
| 페이지 신규/병합 승인 | 인덱스·로그·메타 갱신 |
| `WIKI.md` 룰 수정 | 룰 따라 일관성 유지 |

## 9. 금기 사항 (LLM)

- ❌ `_Sources/` 원천 파일 본문 수정
- ❌ 페이지 자동 삭제 (대신 `status: superseded` 마크)
- ❌ 명시되지 않은 폴더 신설 (사용자 확인 필요)
- ❌ frontmatter 필수 필드 누락
- ❌ wikilink 깨뜨림 (rename 시 모든 inbound 갱신)

## 10. 도구 & 통합

- **Obsidian**: 메인 IDE. Graph View로 토폴로지 확인.
- **Obsidian Web Clipper** (브라우저 확장): 웹 글 → `_Inbox/` 마크다운.
- **Dataview 플러그인**: frontmatter 쿼리 (status/tags/para 필터).
- **scripts/wiki_new_source.sh**: Inbox 스켈레톤 생성.
- **scripts/wiki_status.sh**: orphan/stale 빠른 점검.
- **prompts/{ingest,query,lint}.md**: 워크플로 프롬프트 (Claude에 복붙).

## 11. 확장·진화

- 50+ 소스 누적 시 `index.md` 카테고리 재정렬 검토.
- 200+ 페이지 시 BM25/vector 검색 도구(qmd 등) 도입 고려.
- 도메인 추가 시 새 페이지 타입 정의 (예: `Books/`, `People/` 분리).
- 룰 변경 시 이 파일 갱신 + `log.md`에 변경 이력 기록.
