# CLAUDE.md — Claude Code 전용 지침

공통 규칙은 아래 정본에서 가져옵니다. **공통 내용은 이 파일이 아니라 `AGENTS.md` 를 수정하세요.**

@AGENTS.md

---

## 🍱 노션 루틴 — 스킬 우선

- Claude Code에서는 **`notion-suite` 스킬**(`/notion` 계열: notion-diary, notion-diet-manager, notion-budget)을 `02.Areas/07.Notion-Ops/` SOP보다 **우선 사용**한다.
- SOP 문서는 스킬이 없는 환경(agy/Codex/Gemini)용 폴백 SoT다.
- 스킬과 SOP 내용이 어긋나면 **스킬 최신본 기준으로 SOP를 갱신**한다.

## 🔔 세션 브리핑 자동 주입

- `NEXT-SESSION.md` 는 `.claude/settings.json` 의 SessionStart 훅이 자동으로 컨텍스트에 주입한다 — 별도 Read 없이 브리핑이 이미 로드된 상태로 세션이 시작된다.
