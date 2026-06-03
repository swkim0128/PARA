---
type: concept
para: resource
status: active
sources:
  - "[[2026-06-03 - LLM Wiki 구축 가이드]]"
related:
  - "[[LLM Wiki]]"
  - "[[Andrej Karpathy]]"
tags: [architecture, knowledge-management, separation-of-concerns]
created: 2026-06-03
updated: 2026-06-03
---

# 3-Layer Architecture

[[LLM Wiki]] 패턴의 핵심 구조. **책임의 분리**(separation of concerns) — 인간·LLM·규칙이 각 계층을 독립적으로 다루면서 유기적으로 연결.

## 세 계층

| 계층 | 이름 | 위치 (본 볼트) | 소유 | 수정 권한 |
|---|---|---|---|---|
| 1 | Raw Sources | `03.Resources/Wiki/_Sources/`, `01~04.{PARA}/` | 사용자 | 사용자만 (LLM 읽기 전용) |
| 2 | Wiki | `03.Resources/Wiki/{Entities,Concepts,Topics,Comparisons}/`, `index.md`, `log.md` | LLM | LLM이 생성·갱신·교차참조 |
| 3 | Schema | `03.Resources/Wiki/WIKI.md` | 사용자 | 사용자가 규칙 정의 |

## 불변 규칙

- LLM은 1계층의 원천 파일 본문을 **절대 수정하지 않는다**. 합성·요약은 2계층 별도 페이지로 작성하고 원천은 wikilink만.
- 3계층(스키마)을 수정하면 2계층 LLM 동작이 바뀐다 — 스키마가 곧 LLM의 운영 룰.

## 의의

- 인간은 큐레이션(어떤 자료를 읽을지)·방향 설정에 집중.
- LLM은 지루한 북키핑(요약·교차참조·정리)을 담당.
- 스키마가 협업 인터페이스 역할 — 룰 변경만으로 시스템 진화.

## 관련

- 본 볼트의 [[LLM Wiki]] 구현은 이 아키텍처를 그대로 따른다.
- 사용자-LLM 역할 분담 상세는 `WIKI.md` §8.
