# Claude Desktop & Claude Code 설정 동기화 가이드

> 마지막 업데이트: 2024-12-05

이 디렉토리에는 Claude Desktop에서 사용 중인 MCP 서버와 스킬을 Claude Code에도 적용하기 위한 모든 파일이 포함되어 있습니다.

## 📁 파일 구성

```
04.Claude-Config/
├── README.md                          # 이 파일
├── Claude-Desktop-Configuration.md    # 상세 설정 가이드
├── claude_config_template.json        # MCP 설정 템플릿
├── notion-weekly-schedule-skill.md    # 노션 주간 일정 스킬 문서
├── sync-claude-config.sh             # 자동 동기화 스크립트
└── backups/                          # 설정 파일 백업 디렉토리
```

## 🚀 빠른 시작

### 1. 스크립트 실행 권한 부여
```bash
cd /Users/eunsol/Project/para/02.Areas/04.Claude-Config
chmod +x sync-claude-config.sh
```

### 2. 동기화 스크립트 실행
```bash
./sync-claude-config.sh
```

### 3. Claude Code 재시작

## 📝 MCP 서버 설정

현재 사용 가능한 MCP 서버:
- **filesystem**: 파일 시스템 접근
- **notion**: Notion 통합
- **google-calendar**: Google Calendar 통합
- **google-drive**: Google Drive 통합
- **gmail**: Gmail 통합

## 💾 백업 관리

### 자동 백업
스크립트 실행 시 자동으로 백업 생성

### 수동 백업
```bash
# Claude Desktop 설정 백업
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   backups/claude_desktop_config_$(date +%Y%m%d_%H%M%S).json

# Claude Code 설정 백업
cp ~/.claude/claude_code_config.json \
   backups/claude_code_config_$(date +%Y%m%d_%H%M%S).json
```

### 백업 복원
```bash
# 백업 파일 목록
ls -lt backups/

# 복원
cp backups/claude_desktop_config_YYYYMMDD_HHMMSS.json \
   ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

## 📋 체크리스트

- [ ] Claude Desktop MCP 설정 확인
- [ ] 환경 변수 설정 완료  
- [ ] 동기화 스크립트 실행
- [ ] Claude Code 재시작
- [ ] MCP 서버 연결 확인
- [ ] 스킬 동작 테스트
- [ ] 백업 파일 생성 확인

## 📚 추가 문서

자세한 내용은 다음 문서를 참고하세요:
- `Claude-Desktop-Configuration.md`: 상세 설정 가이드
- `notion-weekly-schedule-skill.md`: 노션 스킬 문서
