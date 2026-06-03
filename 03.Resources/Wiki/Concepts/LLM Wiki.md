---
type: concept
para: resource
status: active
sources:
  - "[[2026-06-03 - LLM Wiki 구축 가이드]]"
related:
  - "[[Andrej Karpathy]]"
  - "[[RAG]]"
  - "[[3-Layer Architecture]]"
  - "[[지식의 복리 효과]]"
  - "[[RAG vs LLM Wiki]]"
  - "[[개인 지식 관리]]"
tags: [knowledge-management, llm, pattern]
created: 2026-06-03
updated: 2026-06-03
---

# LLM Wiki

[[Andrej Karpathy]]가 제안한 **LLM 기반 개인 지식 베이스 패턴**. 사용자가 원천 자료를 큐레이션하면, LLM이 지속적으로 축적·갱신되는 마크다운 위키를 자동 작성·유지한다.

## 핵심 아이디어

> "AI가 지식을 읽고, 정리하고, 연결하고, 유지보수한다. 인간은 아이디어를 탐구하고 질문한다."

기존 [[RAG]]가 매 질문마다 원문에서 조각을 찾는 방식인 데 비해, LLM Wiki는 **사전에 위키로 컴파일**해 두고 질문 시에는 위키만 참조한다. 결과적으로 [[지식의 복리 효과]]가 발생한다.

## 3대 워크플로

| 단계 | 트리거 | LLM 작업 |
|---|---|---|
| **Ingest** | 새 자료를 inbox에 둠 | 읽고 요약 페이지 생성, 관련 엔티티/개념 페이지 10~15개 갱신, 로그 기록 |
| **Query** | 사용자 질문 | 위키 검색·인용 종합 답변, 가치 있으면 새 페이지로 파일링 |
| **Lint** | 주기적 점검 | 모순·고아·누락 개념·오래된 정보·데이터 갭 탐지 |

## 아키텍처

세 계층으로 구성. 상세: [[3-Layer Architecture]]

| 계층 | 역할 |
|---|---|
| Raw Sources (1계층) | 불변 원본. 사용자 큐레이션. |
| Wiki (2계층) | LLM 합성·유지. 본 `03.Resources/Wiki/` 하위. |
| Schema (3계층) | 규칙. 본 볼트의 `WIKI.md`. |

## 본 볼트 구현

- 위치: `03.Resources/Wiki/`
- 스키마: `03.Resources/Wiki/WIKI.md`
- 실행 주체: [[Claude Code]]
- 표시 IDE: [[Obsidian]]
- 수집 도구: [[Obsidian Web Clipper]] → `Clippings/` 또는 `_Inbox/`

## 차별점 vs RAG

전체 비교는 [[RAG vs LLM Wiki]] 참조.

## 적용 가능 영역

개인 일지, 장기 리서치, 책 읽기 노트, 팀 위키, 경쟁 분석·실사 등 **장기간 누적되는 모든 지식 작업**.
