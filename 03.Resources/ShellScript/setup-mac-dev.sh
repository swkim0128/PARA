#!/bin/bash

# ==============================================================================
# [ 스크립트 명 ] : Mac 개발 환경 자동 세팅 스크립트
# [ 작성 목적 ] : 2026 Mac 터미널 & AI 바이브 코딩 환경을 자동으로 구성합니다.
#                기존 설정 파일은 .bak으로 백업 후 덮어씁니다.
#
# [ 필수 요구 사항 ] :
#   - macOS (Apple Silicon 또는 Intel)
#   - 인터넷 연결
#
# [ 실행 방법 ] :
#   chmod +x setup-mac-dev.sh
#   ./setup-mac-dev.sh
# ==============================================================================

set -e  # 오류 발생 시 즉시 중단

# 스크립트 자신의 위치를 기준으로 configs 경로 설정
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIGS_DIR="$SCRIPT_DIR/configs"

# -----------------------------------------------------------------------
# 색상 출력 헬퍼
# -----------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC}   $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
error()   { echo -e "${RED}[ERR]${NC}  $1"; }

backup_if_exists() {
  local file="$1"
  if [[ -f "$file" ]]; then
    cp "$file" "${file}.bak"
    warn "기존 파일 백업: ${file}.bak"
  fi
}

# -----------------------------------------------------------------------
# 0. 시작 메시지
# -----------------------------------------------------------------------
echo ""
echo "============================================================"
echo "  🚀 Mac 개발 환경 자동 세팅 시작"
echo "============================================================"
echo ""

# -----------------------------------------------------------------------
# 1. Homebrew
# -----------------------------------------------------------------------
info "Homebrew 확인 중..."
if ! command -v brew &>/dev/null; then
  info "Homebrew 설치 중..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  # Apple Silicon PATH 설정
  if [[ $(uname -m) == "arm64" ]]; then
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
  fi
  success "Homebrew 설치 완료"
else
  success "Homebrew 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 2. Ghostty 터미널
# -----------------------------------------------------------------------
info "Ghostty 설치 확인 중..."
if ! brew list --cask ghostty &>/dev/null 2>&1 && [[ ! -d "/Applications/Ghostty.app" ]]; then
  info "Ghostty 설치 중..."
  brew install --cask ghostty
  success "Ghostty 설치 완료"
else
  success "Ghostty 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 3. D2Coding 폰트
# -----------------------------------------------------------------------
info "D2Coding 폰트 설치 확인 중..."
if ! brew list --cask font-d2coding &>/dev/null 2>&1; then
  info "D2Coding 폰트 설치 중..."
  brew tap homebrew/cask-fonts 2>/dev/null || true
  brew install --cask font-d2coding 2>/dev/null || warn "font-d2coding cask를 찾을 수 없습니다. https://github.com/naver/d2codingfont 에서 수동 설치하세요."
else
  success "D2Coding 폰트 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 4. CLI 도구 설치
# -----------------------------------------------------------------------
info "CLI 도구 설치 중..."

FORMULAS=(
  lsd bat fzf fd ripgrep git-delta
  btop dust duf fastfetch
  neovim tmux tmuxinator
  zoxide lazygit navi starship mise
  yazi gh jq thefuck
)

for formula in "${FORMULAS[@]}"; do
  if ! brew list --formula "$formula" &>/dev/null 2>&1; then
    info "  설치 중: $formula"
    brew install "$formula"
  else
    info "  이미 설치됨: $formula"
  fi
done

success "CLI 도구 설치 완료"

# -----------------------------------------------------------------------
# 5. Oh My Zsh
# -----------------------------------------------------------------------
info "Oh My Zsh 확인 중..."
if [[ ! -d "$HOME/.oh-my-zsh" ]]; then
  info "Oh My Zsh 설치 중..."
  RUNZSH=no CHSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  success "Oh My Zsh 설치 완료"
else
  success "Oh My Zsh 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 6. Zinit
# -----------------------------------------------------------------------
info "Zinit 확인 중..."
if [[ ! -f "$HOME/.local/share/zinit/zinit.git/zinit.zsh" ]]; then
  info "Zinit 설치 중..."
  mkdir -p "$HOME/.local/share/zinit"
  git clone https://github.com/zdharma-continuum/zinit "$HOME/.local/share/zinit/zinit.git"
  success "Zinit 설치 완료"
else
  success "Zinit 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 7. AI 도구
# -----------------------------------------------------------------------
info "Claude Code 확인 중..."
if ! command -v claude &>/dev/null; then
  info "Claude Code 설치 중..."
  curl -fsSL https://claude.ai/install.sh | bash
  success "Claude Code 설치 완료"
else
  success "Claude Code 이미 설치됨 ($(claude --version 2>/dev/null))"
fi

info "Gemini CLI 확인 중..."
if ! command -v gemini &>/dev/null; then
  info "Gemini CLI 설치 중..."
  brew install gemini-cli
  success "Gemini CLI 설치 완료"
else
  success "Gemini CLI 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 8. Ghostty 설정
# -----------------------------------------------------------------------
info "Ghostty 설정 파일 복사 중..."
mkdir -p ~/.config/ghostty
backup_if_exists ~/.config/ghostty/config
cp "$CONFIGS_DIR/ghostty.config" ~/.config/ghostty/config
success "Ghostty 설정 완료"

# -----------------------------------------------------------------------
# 9. Starship 설정
# -----------------------------------------------------------------------
info "Starship 설정 파일 복사 중..."
mkdir -p ~/.config
backup_if_exists ~/.config/starship.toml
cp "$CONFIGS_DIR/starship.toml" ~/.config/starship.toml
success "Starship 설정 완료"

# -----------------------------------------------------------------------
# 10. .zshrc 설정
# -----------------------------------------------------------------------
info ".zshrc 설정 파일 복사 중..."
backup_if_exists ~/.zshrc
cp "$CONFIGS_DIR/zshrc" ~/.zshrc
success ".zshrc 설정 완료"

# -----------------------------------------------------------------------
# 11. Neovim 설정
# -----------------------------------------------------------------------
info "Neovim 설정 파일 복사 중..."
mkdir -p ~/.config/nvim
backup_if_exists ~/.config/nvim/init.lua
cp "$CONFIGS_DIR/nvim/init.lua" ~/.config/nvim/init.lua
success "Neovim 설정 완료"

# -----------------------------------------------------------------------
# 12. Git Delta 설정
# -----------------------------------------------------------------------
info "Git Delta 설정 중..."
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
git config --global delta.side-by-side true
git config --global delta.line-numbers true
success "Git Delta 설정 완료"

# lazygit 설정
info "Lazygit 설정 파일 복사 중..."
mkdir -p ~/.config/lazygit
backup_if_exists ~/.config/lazygit/config.yml
cp "$CONFIGS_DIR/lazygit/config.yml" ~/.config/lazygit/config.yml
success "Lazygit 설정 완료"

# -----------------------------------------------------------------------
# 14. Tmux TPM (플러그인 매니저)
# -----------------------------------------------------------------------
info "Tmux TPM 확인 중..."
if [[ ! -d "$HOME/.tmux/plugins/tpm" ]]; then
  info "TPM 설치 중..."
  git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
  success "TPM 설치 완료"
else
  success "TPM 이미 설치됨"
fi

# -----------------------------------------------------------------------
# 15. Tmux 설정
# -----------------------------------------------------------------------
info "Tmux 설정 파일 복사 중..."
backup_if_exists ~/.tmux.conf
cp "$CONFIGS_DIR/tmux.conf" ~/.tmux.conf
success "Tmux 설정 완료"
warn "tmux 실행 후 'Prefix + I' 로 플러그인을 설치하세요."

# -----------------------------------------------------------------------
# 완료 메시지
# -----------------------------------------------------------------------
echo ""
echo "============================================================"
echo "  ✅ 모든 설정이 완료되었습니다!"
echo "============================================================"
echo ""
echo "  다음 단계:"
echo "  1. 터미널을 재시작하거나 'source ~/.zshrc' 실행"
echo "  2. Ghostty를 재시작하여 설정 적용"
echo "  3. 'nvim' 실행 → 플러그인 자동 설치 대기"
echo "  4. 'tmux' 실행 → 'Prefix + I' 로 플러그인 설치"
echo "  5. (선택) 'claude auth login' 으로 Claude Code 인증"
echo ""
echo "  백업 파일 위치: 기존 설정파일명.bak"
echo ""

osascript -e 'display notification "Mac 개발 환경 설정이 완료되었습니다. 터미널을 재시작하세요." with title "setup-mac-dev" subtitle "설치 완료 🚀"' 2>/dev/null || true
