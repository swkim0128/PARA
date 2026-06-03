---
type: concept
para: resource
status: stable
sources:
  - "[[2026-06-03 - LLM Wiki 구축 가이드]]"
related:
  - "[[LLM Wiki]]"
  - "[[RAG vs LLM Wiki]]"
  - "[[개인 지식 관리]]"
tags: [retrieval, llm, pattern]
created: 2026-06-03
updated: 2026-06-03
---

# RAG

**Retrieval Augmented Generation**. LLM이 답변 생성 전에 외부 문서 저장소에서 관련 조각(chunk)을 검색해 컨텍스트에 주입하는 패턴. 현재 대부분의 LLM 기반 지식 시스템이 채택.

## 동작 방식

1. 문서를 chunk로 분할 → 임베딩 벡터 저장.
2. 사용자 질문 → 질문 임베딩 ↔ 문서 벡터 유사도 검색.
3. 상위 K개 chunk를 LLM 컨텍스트에 첨부 → 답변 생성.

## 한계

본 위키 컨텍스트에서 [[LLM Wiki]]와 대비되는 약점:

- **지식 축적 없음**: 매 질문마다 처음부터 검색. 누적 효과 없음.
- **문서 간 연결 자동 생성 안 됨**: chunk 단위라 엔티티·개념 그래프 미형성.
- **모순 감지 어려움**: 질문 시점에 함께 검색되어야만 드러남.
- **토큰 비용**: 매 질문마다 다량 chunk 주입 필요.

## 비유

> 매번 도서관에서 책을 찾아 읽는 방식.
> ([[LLM Wiki]] = 사서가 미리 요약해둔 노트 참조)

## 비교

전체 표: [[RAG vs LLM Wiki]]
