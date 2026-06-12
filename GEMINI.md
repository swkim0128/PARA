# My PARA-based Second Brain

This is a personal knowledge management system built on the PARA method.

## Structure

*   **01. Projects:** Active projects with defined goals.
*   **02. Areas:** Long-term areas of responsibility and interest.
*   **03. Resources:** A library of topics and reference materials.
*   **04. Archives:** Inactive items from the other three categories.

---

이 영역은 Gemini/Antigravity 코딩 어시스턴트가 이 저장소의 코드를 다룰 때 참고할 가이드입니다. (CLAUDE.md 설정 기반)

## 버전 관리

이 볼트는 자동 백업을 위해 obsidian-git 플러그인을 사용합니다:
- 커밋 메시지 형식: `DOC: backup {{date}}`
- 자동 커밋 메시지: `vault backup: {{date}}`
- 날짜 형식: `YYYY-MM-DD HH:mm:ss`
- 파일 변경 후 30분마다 자동 저장
- push 전 pull 활성화됨

**수동으로 변경사항을 커밋할 때**는 기존 규칙을 따르세요:
```bash
git add .
git commit -m "DOC: backup $(date '+%Y-%m-%d %H:%M:%S')"
git push
```

## 진행 중인 프로젝트

### OutlineObsidianSync
위치: `1. Project/OutlineObsidianSync/`

Outline(지식 베이스 도구)과 Obsidian 간의 문서 동기화를 위한 Obsidian 플러그인 프로젝트:
- Outline과 로컬 Obsidian 볼트 간의 양방향 동기화 지원
- 데이터 가져오기 및 업데이트를 위해 Outline API 사용
- Obsidian Plugin API를 사용하여 TypeScript로 작성됨
- 주요 기능: API 통합, 파일 충돌 방지, 설정 가능한 동기화 주기

**개발 명령어** (이 프로젝트 작업 시):
- 빌드: `tsc`
- Obsidian에 설치: `dist/` 내용을 `.obsidian/plugins/outline-sync/`에 복사

## Obsidian 설정

이 볼트는 여러 커뮤니티 플러그인을 사용합니다:
- **obsidian-git**: Git 저장소로 자동 백업
- **dataview**: 노트에서 데이터 쿼리 및 표시
- **calendar**: 일일 노트를 위한 달력 뷰
- **templater-obsidian**: 노트용 템플릿 시스템
- **excalidraw**: 다이어그램 및 스케치 도구
- **obsidian-linter**: 마크다운 포맷팅 및 린팅
- **readwise-official**: Readwise 통합

## 마크다운 파일 작업

- 모든 문서는 한국어 마크다운 형식으로 작성됨
- 내부 링크는 Obsidian의 `[[위키-링크]]` 구문 사용
- Excalidraw 다이어그램은 `.excalidraw.md` 확장자 사용
- 볼트 구조는 PARA 방법론을 따름 - 새 파일을 생성할 때 이 구조를 준수할 것

## 파일 구조 규칙

- PARA 카테고리에 번호 접두사 사용: `1. Project/`, `2. Area/`, `3. Resource/`, `4. Archive/`
- 리소스 노트는 주제별로 정리됨 (Algorithm, JavaScript, React, TypeScript, Kotlin 등)
- 각 리소스 주제는 메인 개요 파일을 가짐 (예: `알고리즘 정리.md`, `Javascript 정리.md`)
- 프로젝트 폴더는 프로젝트별 문서 및 계획 파일 포함

## 태스크 및 대시보드

### TASKS.md
위치: 루트 `TASKS.md`

GTD 스타일의 프로젝트/태스크 추적 파일:
- **Active**: 진행 중인 태스크 (상태, 우선순위, Notion 링크 포함)
- **Waiting On**: 대기 중인 항목
- **Someday**: 언жен가 할 항목
- **Done**: 완료된 프로젝트 이력

### dashboard.html
위치: 루트 `dashboard.html`

TASKS.md 기반의 생산성 대시보드 UI 파일