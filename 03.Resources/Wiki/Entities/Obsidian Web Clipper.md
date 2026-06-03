---
type: entity
para: resource
status: active
sources:
  - "[[2026-06-03 - LLM Wiki 구축 가이드]]"
related:
  - "[[Obsidian]]"
  - "[[LLM Wiki]]"
tags: [tool, browser-extension, ingestion]
created: 2026-06-03
updated: 2026-06-03
---

# Obsidian Web Clipper

브라우저(Chrome 등) 확장 프로그램. 웹 페이지를 클릭 한 번에 마크다운으로 저장하여 [[Obsidian]] 볼트의 지정 폴더로 배치한다. 본 위키의 **원천 자료 수집 진입점**.

## 본 위키와의 역할

- 출력 폴더를 `Clippings/`(또는 `03.Resources/Wiki/_Inbox/`)로 지정 → [[LLM Wiki]] Ingest 워크플로 입력.
- 자동 생성되는 frontmatter (`title`, `source`, `author`, `published`, `created`, `description`, `tags`) 가 후속 합성 페이지의 메타 단서로 사용된다.
- 본 위키의 첫 ingest 대상([[2026-06-03 - LLM Wiki 구축 가이드]])이 이 도구로 수집됨.

## 외부 링크

- Chrome Web Store: https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf
