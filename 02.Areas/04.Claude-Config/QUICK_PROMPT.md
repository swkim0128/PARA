# Claude Code 실행 프롬프트

다음 작업을 수행해주세요:

## 1. 프로젝트 생성
`~/Projects/claude-config-sync` 프로젝트를 다음 구조로 생성:
```
claude-config-sync/
├── README.md
├── skills/notion-weekly-schedule/
├── mcp-configs/
├── scripts/
└── backups/
```

## 2. 파일 이동
다음 파일들을 복사하고 적절히 수정:

**소스:** `/Users/eunsol/Project/para/02.Areas/04.Claude-Config/`
- `claude_config_template.json` → `mcp-configs/claude_desktop_config.json`
- `sync-claude-config.sh` → `scripts/sync-claude-config.sh` (경로 수정 필요)
- `/mnt/skills/user/notion-weekly-schedule/SKILL.md` → `skills/notion-weekly-schedule/SKILL.md`

## 3. 스크립트 수정
`scripts/sync-claude-config.sh`에서:
- `SCRIPT_DIR` → `PROJECT_ROOT="$HOME/Projects/claude-config-sync"`로 변경
- `BACKUP_DIR="$PROJECT_ROOT/backups"`로 수정
- 모든 경로를 프로젝트 루트 기준으로 업데이트

## 4. 추가 파일 생성
- `README.md`: 프로젝트 개요 및 사용법
- `.gitignore`: 백업 파일, 환경 변수 제외
- `backups/.gitkeep`: 백업 디렉토리 유지

## 5. 권한 설정
```bash
chmod +x ~/Projects/claude-config-sync/scripts/sync-claude-config.sh
```

## 6. Areas 정리
`/Users/eunsol/Project/para/02.Areas/04.Claude-Config/README.md` 업데이트:
- 실제 프로젝트 위치 안내
- `~/Projects/claude-config-sync` 링크 추가

---

자세한 요구사항은 `CLAUDE_CODE_PROMPT.md` 참조
