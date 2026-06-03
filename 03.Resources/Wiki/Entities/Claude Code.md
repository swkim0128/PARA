---
type: entity
para: resource
status: active
sources:
  - "[[2026-06-03 - LLM Wiki 구축 가이드]]"
related:
  - "[[Obsidian]]"
  - "[[LLM Wiki]]"
  - "[[Obsidian Web Clipper]]"
tags: [ai, cli, anthropic, tool]
created: 2026-06-03
updated: 2026-06-03
---

# Claude Code

Anthropic이 제공하는 공식 CLI 도구. 터미널·데스크탑 앱·웹 앱·IDE 확장으로 사용 가능. 본 위키에서는 **Ingest/Query/Lint 워크플로의 실행 주체**로 활용된다.

## 본 위키와의 역할

- 사용자가 `_Inbox/` 또는 `Clippings/`에 원천 자료를 두면 Claude Code가 읽고 [[LLM Wiki]] 페이지를 합성·갱신.
- `WIKI.md` 스키마 규칙을 컨텍스트로 받아 일관성 있게 페이지를 생성·교차 참조한다.
- 사용자 질문에 위키를 검색하여 인용 포함 답변을 제공한다.

## 관련 도구

- [[Obsidian]] — 위키의 표시·편집 IDE
- [[Obsidian Web Clipper]] — 원천 자료 수집 브라우저 확장

## 외부 링크

- 공식 사이트: https://claude.com/claude-code
