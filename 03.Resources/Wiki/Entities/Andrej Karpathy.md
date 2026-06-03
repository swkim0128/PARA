---
type: entity
para: resource
status: active
sources:
  - "[[2026-06-03 - LLM Wiki 구축 가이드]]"
related:
  - "[[LLM Wiki]]"
  - "[[RAG]]"
  - "[[3-Layer Architecture]]"
tags: [ai, researcher, llm]
created: 2026-06-03
updated: 2026-06-03
---

# Andrej Karpathy

AI 분야 연구자·실무가. OpenAI 창립 멤버, Tesla AI 디렉터를 거쳐 독립 활동 중. 본 위키 운영 패러다임의 원안인 **[[LLM Wiki]]** 패턴을 [공개 gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)로 제안했다.

## 본 위키와의 관계

- 카파시가 제안한 LLM Wiki 패턴이 본 `03.Resources/Wiki/` 운영 스키마(`WIKI.md`)의 직접적 출처.
- 핵심 주장: "AI가 지식을 읽고·정리하고·연결하고·유지보수한다. 인간은 아이디어를 탐구하고 질문한다."
- [[RAG]] 한계 극복 대안으로 **사전 컴파일된 마크다운 위키**를 제시.

## 주요 아이디어

- **3-Layer Architecture**: Raw Sources(불변) / Wiki(LLM 소유) / Schema(규칙) — 책임 분리. → [[3-Layer Architecture]]
- **Ingest / Query / Lint** 3대 워크플로로 위키 유지보수 작업을 LLM에 위임.
- **복리 효과**: 시간이 지날수록 지식 그래프가 풍부해지는 누적 효과.

## 출처

- gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 본 위키 도입 경로: [[2026-06-03 - LLM Wiki 구축 가이드]] (James AI Explorer 해설 글)
