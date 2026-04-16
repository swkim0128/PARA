#!/bin/bash

set -e

BACKUP_DIR="$HOME/Project/para/03.Resources/ShellScript/vibe-coding-backup"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC}   $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }

echo ""
echo "============================================================"
echo "  🚀 Vibe Coding 환경 백업 시작"
echo "============================================================"
echo ""

# -----------------------------------------------------------------------
# 1. 디렉토리 생성
# -----------------------------------------------------------------------
info "백업 디렉토리 생성 중..."
mkdir -p "$BACKUP_DIR/tmux-scripts"
mkdir -p "$BACKUP_DIR/nvim-lua"
mkdir -p "$BACKUP_DIR/claude-config/hooks"
success "디렉토리 구조 생성 완료"

# -----------------------------------------------------------------------
# 2. Tmux 및 워크플로우 스크립트 복사
# -----------------------------------------------------------------------
info "Tmux 및 워크플로우 스크립트 복사 중..."
cp ~/.tmux.conf              "$BACKUP_DIR/tmux-scripts/tmux.conf"
cp ~/.config/vibe-tools/tmux-sessionizer.sh    "$BACKUP_DIR/tmux-scripts/tmux-sessionizer.sh"
cp ~/.config/vibe-tools/claude-skills.sh       "$BACKUP_DIR/tmux-scripts/claude-skills.sh"
cp ~/.config/vibe-tools/my-tools.sh            "$BACKUP_DIR/tmux-scripts/my-tools.sh"
cp ~/.config/vibe-tools/claude-delegate.sh     "$BACKUP_DIR/tmux-scripts/claude-delegate.sh"
cp ~/.config/vibe-tools/claude-callback.sh     "$BACKUP_DIR/tmux-scripts/claude-callback.sh"
success "tmux-scripts/ 복사 완료"

# -----------------------------------------------------------------------
# 3. Neovim (NvChad) 커스텀 설정 복사
# -----------------------------------------------------------------------
info "Neovim lua 설정 복사 중..."
cp -r ~/.config/nvim/lua/. "$BACKUP_DIR/nvim-lua/"
success "nvim-lua/ 복사 완료"

# -----------------------------------------------------------------------
# 4. Claude Code 설정 복사
# -----------------------------------------------------------------------
info "Claude Code 설정 복사 중..."
# 실제 파일 위치: ~/.config/vibe-tools/claude-config/ (symlink로 ~/.claude/에 연결됨)
cp ~/.config/vibe-tools/claude-config/settings.json          "$BACKUP_DIR/claude-config/settings.json"
cp ~/.config/vibe-tools/claude-config/hooks/mac-notify.sh    "$BACKUP_DIR/claude-config/hooks/mac-notify.sh"
success "claude-config/ 복사 완료"

# -----------------------------------------------------------------------
# 5. README.md 생성
# -----------------------------------------------------------------------
info "README.md 생성 중..."
cat > "$BACKUP_DIR/README.md" << 'README_EOF'
# Vibe Coding 개발 환경 백업

이 저장소는 바이브 코딩 환경(Tmux + Neovim + Claude Code)의 핵심 설정 파일 백업입니다.

---

## 📁 디렉토리 구조

```
vibe-coding-backup/
├── tmux-scripts/          # Tmux 설정 및 워크플로우 스크립트
├── nvim-lua/              # Neovim (NvChad) 커스텀 lua 설정
├── claude-config/         # Claude Code 설정 및 알림 훅
└── README.md
```

---

## 🖥️ tmux-scripts/

| 파일 | 복원 위치 | 역할 |
|------|-----------|------|
| `tmux.conf` | `~/.tmux.conf` | Tmux 전체 설정 (Catppuccin Macchiato 테마, 단축키, Resurrect/Continuum) |
| `tmux-sessionizer.sh` | `~/.config/vibe-tools/tmux-sessionizer.sh` | 프로젝트 선택 시 nvim 70% + claude 30% 레이아웃 자동 구성 (`Prefix+F`) |
| `claude-skills.sh` | `~/.config/vibe-tools/claude-skills.sh` | 현재 세션에서 Claude 패널을 자동 탐지하여 스킬 프롬프트 전송 (`Prefix+C`) |
| `my-tools.sh` | `~/.config/vibe-tools/my-tools.sh` | fzf 기반 자주 쓰는 명령어 팝업 메뉴 (`Prefix+M`, `Ctrl+F`) |
| `claude-delegate.sh` | `~/.config/vibe-tools/claude-delegate.sh` | 다른 tmux 패널의 클로드에게 작업 위임 + 콜백 요청 (IPC) |
| `claude-callback.sh` | `~/.config/vibe-tools/claude-callback.sh` | 작업 완료 후 지휘관 패널에 결과 보고 (IPC) |

### Tmux 주요 단축키

| 단축키 | 기능 |
|--------|------|
| `Prefix` | `Ctrl+Space` (Ctrl+b도 유지) |
| `Prefix + F` | 프로젝트 세션 매니저 (tmux-sessionizer) |
| `Prefix + C` | Claude 스킬 팝업 |
| `Prefix + M` | 커스텀 명령어 팝업 |
| `Prefix + P` | 프로젝트 점프 (project-jump) |
| `Prefix + Tab` | yazi 파일탐색기 |
| `Option + hjkl` | 패널 이동 |
| `m70` / `m50` | 패널 비율 조정 |

---

## ✏️ nvim-lua/

NvChad 기반 Neovim 커스텀 설정입니다 (`~/.config/nvim/lua/` 전체 백업).

| 파일 | 역할 |
|------|------|
| `chadrc.lua` | NvChad 커스터마이징 (catppuccin 테마, 투명 배경, 상태바) |
| `options.lua` | 줄 번호, 들여쓰기, clipboard, tmux ESC 딜레이 제거 |
| `mappings.lua` | 파일 탐색기, 버퍼 이동 단축키 |
| `plugins/init.lua` | 추가 플러그인 (Mason LSP, Treesitter, vim-slime tmux 연동) |
| `autocmds.lua` | 저장 시 줄 끝 공백 자동 제거 (마크다운 제외) |
| `configs/conform.lua` | 저장 시 자동 포매터 (lua/css/html/python/php) |
| `configs/lspconfig.lua` | LSP 서버 설정 |

---

## 🤖 claude-config/

실제 파일 위치: `~/.config/vibe-tools/claude-config/` (심볼릭 링크로 `~/.claude/`에 연결)

| 파일 | 복원 위치 | 역할 |
|------|-----------|------|
| `settings.json` | `~/.config/vibe-tools/claude-config/settings.json` | Claude Code 플러그인, hooks 설정 |
| `hooks/mac-notify.sh` | `~/.config/vibe-tools/claude-config/hooks/mac-notify.sh` | 작업 완료 시 macOS 알림 표시 |

### Claude Code Hooks

| 이벤트 | 동작 |
|--------|------|
| `Stop` | Glass.aiff 사운드 재생 |
| `Notification` | Ping.aiff 재생 + macOS 알림 표시 |

---

## 🔄 복원 방법

```bash
# tmux 설정
cp tmux-scripts/tmux.conf ~/.tmux.conf
mkdir -p ~/.config/vibe-tools
cp tmux-scripts/tmux-sessionizer.sh ~/.config/vibe-tools/tmux-sessionizer.sh && chmod +x ~/.config/vibe-tools/tmux-sessionizer.sh
cp tmux-scripts/claude-skills.sh    ~/.config/vibe-tools/claude-skills.sh    && chmod +x ~/.config/vibe-tools/claude-skills.sh
cp tmux-scripts/my-tools.sh         ~/.config/vibe-tools/my-tools.sh         && chmod +x ~/.config/vibe-tools/my-tools.sh
cp tmux-scripts/claude-delegate.sh  ~/.config/vibe-tools/claude-delegate.sh  && chmod +x ~/.config/vibe-tools/claude-delegate.sh
cp tmux-scripts/claude-callback.sh  ~/.config/vibe-tools/claude-callback.sh  && chmod +x ~/.config/vibe-tools/claude-callback.sh

# Neovim (NvChad) 설정
# ⚠️ 반드시 NvChad를 먼저 설치한 후 lua 설정을 복원하세요
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
# nvim 종료 후:
cp -r nvim-lua/. ~/.config/nvim/lua/

# Claude Code 설정 (vibe-tools로 복원 후 symlink 연결)
mkdir -p ~/.config/vibe-tools/claude-config/hooks
cp claude-config/settings.json          ~/.config/vibe-tools/claude-config/settings.json
cp claude-config/hooks/mac-notify.sh    ~/.config/vibe-tools/claude-config/hooks/mac-notify.sh
chmod +x ~/.config/vibe-tools/claude-config/hooks/mac-notify.sh
# symlink: ~/.claude/ → ~/.config/vibe-tools/claude-config/
ln -sf ~/.config/vibe-tools/claude-config/settings.json ~/.claude/settings.json
ln -sf ~/.config/vibe-tools/claude-config/hooks         ~/.claude/hooks
```
README_EOF
success "README.md 생성 완료"

# -----------------------------------------------------------------------
# 6. Git 초기화 및 커밋
# -----------------------------------------------------------------------
info "Git 저장소 초기화 중..."
cd "$BACKUP_DIR"
git init -q
git add .
git commit -q -m "Initial Vibe Coding Setup Backup"
success "Git 저장소 초기화 및 커밋 완료"

# -----------------------------------------------------------------------
# 완료
# -----------------------------------------------------------------------
echo ""
echo "============================================================"
echo "  ✅ 백업 완료!"
echo "============================================================"
echo ""
echo "  백업 위치: $BACKUP_DIR"
echo ""
git -C "$BACKUP_DIR" log --oneline
echo ""
find "$BACKUP_DIR" -not -path '*/.git/*' | sort | sed "s|$BACKUP_DIR||" | sed 's|^/||'
echo ""
