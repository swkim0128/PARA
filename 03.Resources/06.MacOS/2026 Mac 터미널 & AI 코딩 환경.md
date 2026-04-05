# 2026 Mac 터미널 & AI 바이브 코딩 완벽 세팅 가이드

회사 Mac PC를 처음 지급받았을 때, 이 문서의 순서대로 복사-붙여넣기만 하시면 현재 실제 운용 중인 개발 환경을 즉시 재현할 수 있습니다.

---

## Phase 1. 기본 패키지 설치

기본 터미널(Terminal.app)을 열고 아래 명령어를 순서대로 실행합니다.

```bash
# 1. Homebrew 설치 (없는 경우)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 터미널 설치
brew install --cask ghostty

# 3. 폰트 설치 (D2Coding)
brew install --cask font-d2coding
# 또는 수동으로 D2Coding / D2Coding Ligature 설치: https://github.com/naver/d2codingfont

# 4. 모던 CLI 도구 설치
brew install lsd bat fzf fd ripgrep git-delta btop dust duf fastfetch neovim tmux
brew install zoxide lazygit navi starship mise

# 5. Oh My Zsh 설치
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 6. Zinit 설치
mkdir -p "$HOME/.local/share/zinit"
git clone https://github.com/zdharma-continuum/zinit "$HOME/.local/share/zinit/zinit.git"

# 7. AI 코딩 도구 설치
curl -fsSL https://claude.ai/install.sh | bash   # Claude Code (네이티브)
brew install gemini-cli                           # Gemini CLI
```

---

## Phase 2. 터미널 UI & 셸 환경 설정

### 1. Ghostty 터미널 설정

```bash
mkdir -p ~/.config/ghostty
nano ~/.config/ghostty/config
```

```properties
# ~/.config/ghostty/config

# Theme
theme = Catppuccin Macchiato

# --- 폰트 및 렌더링 ---
font-size = 14
font-family = "D2Coding"
font-family = "D2Coding Ligature"

# 리가처(Ligatures) 활성화
font-feature = "calt"
font-feature = "liga"

# --- 윈도우 UI ---
window-decoration = true
window-padding-x = 10
window-padding-y = 10
window-theme = system

# --- 배경 ---
background-opacity = 0.9
background-blur-radius = 15

# Autosuggestion color (가독성을 위해 밝게)
palette = 8=#7f849c

# --- 커서 설정 ---
cursor-style = block
cursor-style-blink = true

# Mouse
mouse-hide-while-typing = true

# Clipboard
copy-on-select = true
clipboard-paste-protection = false

# Scrollback
scrollback-limit = 10000

# macOS
macos-option-as-alt = true

# Shell Integration
shell-integration = zsh

# 터미널 종료 시 확인 창 비활성화
confirm-close-surface = false
```

### 2. Starship 프롬프트 설정

```bash
mkdir -p ~/.config
nano ~/.config/starship.toml
```

```toml
# ~/.config/starship.toml
"$schema" = 'https://starship.rs/config-schema.json'

format = """
[░▒▓](#a3aed2)\
[  ](bg:#a3aed2 fg:#090c0c)\
[](bg:#769ff0 fg:#a3aed2)\
$directory\
[](fg:#769ff0 bg:#394260)\
$git_branch\
$git_status\
[](fg:#394260 bg:#212736)\
$nodejs\
$rust\
$golang\
$php\
[](fg:#212736 bg:#1d2230)\
$time\
[ ](fg:#1d2230)\
\n$character"""

[directory]
style = "fg:#e3e5e5 bg:#769ff0"
format = "[ $path ]($style)"
truncation_length = 3
truncation_symbol = "…/"

[directory.substitutions]
"Documents" = "󰈙 "
"Downloads" = " "
"Music" = " "
"Pictures" = " "

[git_branch]
symbol = ""
style = "bg:#394260"
format = '[[ $symbol $branch ](fg:#769ff0 bg:#394260)]($style)'

[git_status]
style = "bg:#394260"
format = '[[($all_status$ahead_behind )](fg:#769ff0 bg:#394260)]($style)'

[nodejs]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[rust]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[golang]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[php]
symbol = ""
style = "bg:#212736"
format = '[[ $symbol ($version) ](fg:#769ff0 bg:#212736)]($style)'

[time]
disabled = false
time_format = "%R"
style = "bg:#1d2230"
format = '[[  $time ](fg:#a0a9cb bg:#1d2230)]($style)'
```

### 3. Zsh 셸 통합 설정 (~/.zshrc)

```bash
nano ~/.zshrc
```

```bash
# ~/.zshrc

# 터미널 시작 시 시스템 정보 표시
if [[ $- == *i* ]] && command -v fastfetch &>/dev/null; then
  fastfetch
fi

# Oh My Zsh
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"  # Starship이 override하므로 실질적으로 미사용
plugins=(git)
source $ZSH/oh-my-zsh.sh

# Starship 프롬프트
eval "$(starship init zsh)"

# Zinit 플러그인 매니저
if [[ ! -f $HOME/.local/share/zinit/zinit.git/zinit.zsh ]]; then
    mkdir -p "$HOME/.local/share/zinit"
    git clone https://github.com/zdharma-continuum/zinit "$HOME/.local/share/zinit/zinit.git"
fi
source "$HOME/.local/share/zinit/zinit.git/zinit.zsh"
autoload -Uz _zinit
(( ${+_comps} )) && _comps[zinit]=_zinit

# Zinit annexes (필수)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

# 필수 플러그인 3종
zinit light zdharma-continuum/fast-syntax-highlighting  # 명령어 구문 강조
zinit light zsh-users/zsh-autosuggestions               # 히스토리 기반 자동 완성
zinit light zsh-users/zsh-completions                   # 추가 자동 완성 정의

# fzf + zoxide + navi
if command -v fzf &>/dev/null; then
  source <(fzf --zsh)
fi
if command -v zoxide &>/dev/null; then
  eval "$(zoxide init --cmd cd zsh)"
fi
if command -v navi &>/dev/null; then
  eval "$(navi widget zsh)"
fi

# mise (런타임 버전 관리자)
eval "$(mise activate zsh)"

# Claude Code PATH
export PATH="$HOME/.local/bin:$PATH"

# fzf 기반 도구 런처
function tools() {
  local cmds=(
    "btop:🖥️  시스템 모니터링"
    "lazygit:📦 Git UI"
    "duf:💾 디스크 사용량"
    "dust:📁 폴더 크기 분석"
    "fastfetch:ℹ️  시스템 정보"
  )
  local selected=$(printf '%s\n' "${cmds[@]}" | fzf --delimiter=: --with-nth=2 --height=40% --reverse --border --prompt="도구 선택: ")
  local cmd="${selected%%:*}"
  [[ -n "$cmd" ]] && eval "$cmd"
}

# alias
alias vim="nvim"
alias vi="nvim"
alias lg="lazygit"

# Editor
export EDITOR="nvim"
```

저장 후 `source ~/.zshrc`를 입력하여 적용합니다.

### 4. Tmux 설정

```bash
# TPM (Tmux Plugin Manager) 설치
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

nano ~/.tmux.conf
```

```bash
# === Prefix 변경 (Ctrl+Space, Ctrl+b도 유지) ===
set -g prefix C-Space
set -g prefix2 C-b
bind C-Space send-prefix

# ==========================================
# ✨ Neovim & 바이브 코딩 필수 추가 설정 ✨
# ==========================================
set -sg escape-time 10            # Neovim에서 ESC 누를 때 딜레이 제거
set -g focus-events on            # Neovim 파일 자동 새로고침(Autoread)을 위한 포커스 감지
set -g base-index 1               # 윈도우(탭) 번호를 1부터 시작
setw -g pane-base-index 1         # 패널 번호를 1부터 시작
set -g renumber-windows on        # 중간 탭을 닫으면 번호를 자동으로 다시 매김

# === 기본 설정 ===
set-option -g history-limit 50000
bind % split-window -h -c "#{pane_current_path}"
bind '"' split-window -v -c "#{pane_current_path}"
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"
set -g automatic-rename off
set -g mouse on
set -g allow-passthrough on
set -g pane-border-format " #{pane_index} #{pane_current_command} "
set -g pane-border-status top
set -g pane-border-lines double

# === 복사 모드 (vi) ===
setw -g mode-keys vi
bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "pbcopy"
bind-key -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "pbcopy"
bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-no-clear "pbcopy"
# 마우스 스크롤 속도 (기본 3 → 5줄씩)
bind-key -T copy-mode-vi WheelUpPane send-keys -X -N 5 scroll-up
bind-key -T copy-mode-vi WheelDownPane send-keys -X -N 5 scroll-down

# === 플러그인 ===
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'catppuccin/tmux'
set -g @plugin 'tmux-plugins/tmux-cpu'
set -g @plugin 'tmux-plugins/tmux-battery'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# yazi 파일 탐색기 (Prefix + Tab: 50% 분할)
bind Tab split-window -h -l 50% -c "#{pane_current_path}" "yazi"

# === Catppuccin 테마 ===
set -g @catppuccin_flavor 'mocha'
set -g @catppuccin_window_status_style 'rounded'

set -g @catppuccin_status_background "#363a4f"
set -g status-style bg=default,fg=white

# 상태 바 왼쪽: 세션 이름
set -g status-left-length 40
set -g status-left "#{E:@catppuccin_status_session}"

# 상태 바 오른쪽: 디렉토리 + Git 브랜치 + CPU + 메모리 + 배터리 + 시간
set -g status-right-length 150
set -g @catppuccin_date_time_text " %m/%d %H:%M"

set -g status-right "#{E:@catppuccin_status_directory}"

set -ag status-right "#[bg=default] #[fg=#a6da95,bg=#363a4f] #(cd #{pane_current_path}; git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '-') "
set -ag status-right "#[bg=default] #[fg=#8aadf4,bg=#363a4f] #{cpu_percentage} "
set -ag status-right "#[bg=default] #[fg=#eed49f,bg=#363a4f] #{ram_percentage} "
set -ag status-right "#[bg=default] #[fg=#f5bde6,bg=#363a4f] #{battery_icon} #{battery_percentage} "

set -ag status-right "#{E:@catppuccin_status_date_time}"

# 윈도우 탭 (현재 선택 윈도우 강조)
set -g @catppuccin_window_text " #I:#{=10:window_name} "
set -g @catppuccin_window_current_text " #[bold] *#I:#W* "

# === Pane 이동 (Option + hjkl, prefix 없이) ===
bind -n M-h select-pane -L
bind -n M-j select-pane -D
bind -n M-k select-pane -U
bind -n M-l select-pane -R
bind L last-window
bind r source-file ~/.tmux.conf \; display "Reloaded!"

# ---------------------------------------------------------
# [명령어 Alias(별명) 설정]
# ---------------------------------------------------------
# 명령어 창에서 'm70'을 치면 패널을 70%로 맞춥니다.
set -sa command-alias 'm70=resize-pane -t 1 -x 70%'
# 명령어 창에서 'm50'을 치면 화면을 정확히 반반으로 나눕니다.
set -sa command-alias 'm50=select-layout even-horizontal'
# 명령어 창에서 'killall'을 치면 현재 세션의 모든 패널/윈도우를 종료합니다.
set -sa command-alias 'killall=kill-session'

# ---------------------------------------------------------
# ✨ [Tmux 세션 자동 저장 및 복구 (Resurrect & Continuum)] ✨
# ---------------------------------------------------------
# Neovim 세션(열려있던 파일들)까지 함께 복구하도록 설정
set -g @resurrect-strategy-nvim 'session'
# 패널 안의 프로그램(클로드 코드 등)도 가능하면 살려내기
set -g @resurrect-processes 'claude nvim npm yazi'
# 컴퓨터를 켜고 Tmux를 처음 실행할 때, 마지막 세션을 자동으로 띄움
set -g @continuum-restore 'on'
# 15분마다 백그라운드에서 자동으로 현재 상태를 저장함 (단위: 분)
set -g @continuum-save-interval '15'

# === TPM 실행 ===
run '~/.tmux/plugins/tpm/tpm'
```

저장 후 tmux를 실행하고 `Prefix + I`로 플러그인을 설치합니다.

### 5. Git Delta 설정

`git-delta`는 git diff/log 출력을 문법 강조 + 라인 번호 + side-by-side 뷰로 렌더링해주는 도구입니다.

```bash
# git-delta는 Phase 1의 brew install 명령에 포함되어 있습니다.
# 아래 git 전역 설정을 추가합니다.

git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
git config --global delta.side-by-side true
git config --global delta.line-numbers true
```

`~/.gitconfig`에 다음 내용이 추가됩니다:

```ini
[core]
    pager = delta
[interactive]
    diffFilter = delta --color-only
[delta]
    navigate = true
    side-by-side = true
    line-numbers = true
```

lazygit에서도 delta를 사용하려면 `~/.config/lazygit/config.yml`을 생성합니다:

```bash
mkdir -p ~/.config/lazygit
nano ~/.config/lazygit/config.yml
```

```yaml
# ~/.config/lazygit/config.yml
git:
  pagers:
    - colorArg: always
      pager: delta --dark --paging=never --side-by-side --line-numbers
```

---

## Phase 3. Neovim 설정 (init.lua)

tmux와 통합된 바이브 코딩 환경 + LSP 자동 완성이 포함된 설정입니다.

```bash
mkdir -p ~/.config/nvim
nano ~/.config/nvim/init.lua
```

```lua
-- ==========================================
-- 1. 기본 UI 및 줄 번호 설정
-- ==========================================
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true
vim.opt.termguicolors = true

-- ==========================================
-- 2. 들여쓰기 설정
-- ==========================================
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

-- ==========================================
-- 3. 검색 설정
-- ==========================================
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.hlsearch = false

-- ==========================================
-- 4. 시스템 연동
-- ==========================================
vim.opt.clipboard = "unnamedplus"
vim.opt.mouse = "a"
vim.opt.runtimepath:append(vim.fn.stdpath("data") .. "/site")

-- ==========================================
-- 5. 리더 키
-- ==========================================
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- ==========================================
-- 6. 플러그인 매니저 (lazy.nvim) 자동 설치
-- ==========================================
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- ==========================================
-- 7. 플러그인 목록
-- ==========================================
require("lazy").setup({

  -- [1] 하단 상태 표시줄
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    config = function()
      require('lualine').setup()
    end
  },

  -- [2] 색상 테마 (Ghostty Catppuccin Macchiato와 동일)
  {
    "catppuccin/nvim", name = "catppuccin", priority = 1000,
    config = function()
      require("catppuccin").setup({
        flavour = "mocha",
        transparent_background = true,
        term_colors = true,
      })
      vim.cmd.colorscheme "catppuccin"
    end
  },

  -- [3] 파일 탐색기
  {
    "nvim-tree/nvim-tree.lua", version = "*", lazy = false,
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("nvim-tree").setup {}
      vim.keymap.set('n', '<leader>e', ':NvimTreeToggle<CR>', { noremap = true, silent = true })
    end,
  },

  -- [4] 코드 구문 강조 (Treesitter)
  {
    "nvim-treesitter/nvim-treesitter", build = ":TSUpdate",
    config = function()
      require("nvim-treesitter").setup({
        ensure_installed = {
          "c", "lua", "vim", "vimdoc", "query",
          "python", "javascript", "typescript", "html", "css", "json",
          "kotlin", "php", "java"
        },
        auto_install = true,
        highlight = { enable = true, additional_vim_regex_highlighting = false },
      })
    end,
  },

  -- [5] 파일/텍스트 검색 (Telescope)
  {
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      local builtin = require('telescope.builtin')
      vim.keymap.set('n', '<leader>ff', builtin.find_files, { desc = '파일 찾기' })
      vim.keymap.set('n', '<leader>fg', builtin.live_grep, { desc = '텍스트 검색' })
      vim.keymap.set('n', '<leader>fb', builtin.buffers, { desc = '열려있는 파일' })
    end,
  },

  -- [6] LSP 및 자동 완성
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
      "hrsh7th/nvim-cmp",
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "saadparwaiz1/cmp_luasnip",
      "L3MON4D3/LuaSnip",
      "rafamadriz/friendly-snippets",
    },
    config = function()
      require("mason").setup()
      local servers = { "lua_ls", "ts_ls", "jdtls", "kotlin_language_server", "intelephense", "marksman" }
      require("mason-lspconfig").setup({ ensure_installed = servers })

      local capabilities = require("cmp_nvim_lsp").default_capabilities()
      for _, server in ipairs(servers) do
        vim.lsp.config(server, { capabilities = capabilities })
        vim.lsp.enable(server)
      end

      require("luasnip.loaders.from_vscode").lazy_load()

      local cmp = require("cmp")
      cmp.setup({
        snippet = { expand = function(args) require('luasnip').lsp_expand(args.body) end },
        mapping = cmp.mapping.preset.insert({
          ['<C-Space>'] = cmp.mapping.complete(),
          ['<CR>'] = cmp.mapping.confirm({ select = true }),
          ['<Tab>'] = cmp.mapping.select_next_item(),
          ['<S-Tab>'] = cmp.mapping.select_prev_item(),
        }),
        sources = cmp.config.sources({
          { name = 'nvim_lsp' },
          { name = 'luasnip' },
          { name = 'buffer' },
          { name = 'path' },
        })
      })
    end,
  },

  -- [7] 바이브 코딩 - tmux 창으로 텍스트 전송 (vim-slime)
  {
    "jpalardy/vim-slime",
    init = function()
      vim.g.slime_target = "tmux"
      vim.g.slime_dont_ask_default = 0
      vim.g.slime_default_config = { socket_name = "default", target_pane = "{last}" }
    end,
    config = function()
      vim.keymap.set("x", "<leader>s", "<Plug>SlimeRegionSend", { desc = "선택 영역 tmux로 전송" })
      vim.keymap.set("n", "<leader>s", "<Plug>SlimeParagraphSend", { desc = "현재 문단 tmux로 전송" })
    end,
  },
})
```

`nvim` 실행 시 플러그인과 LSP가 자동 다운로드됩니다.

---

## Phase 4. 커스텀 도구 스크립트

tmux 팝업 메뉴와 Claude Code 연동을 위한 두 가지 스크립트입니다.

### ~/.my-tools.sh — 나만의 명령어 팝업 메뉴

fzf로 자주 쓰는 명령어를 선택·실행합니다.

- **tmux 단축키:** `Prefix + M`
- **zsh 단축키:** `Ctrl + F`

```bash
# 명령어 목록은 "화면에 보일 이름 | 실제 명령어" 형식으로 추가
COMMANDS="
🤖 Claude Code: 현재 프로젝트 분석 | claude -p '이 프로젝트의 구조와 핵심 로직을 분석해서 요약해줘'
🛠️  Tmux 설정 새로고침 | tmux source-file ~/.tmux.conf
🌐 로컬 서버 시작 (예시) | npm run dev
🧹 Docker 사용하지 않는 자원 정리 | docker system prune -af
📂 NvChad 설정 폴더로 이동 | cd ~/.config/nvim && nvim .
"
```

### ~/.project-jump.sh — 프로젝트 빠른 이동

`~/Projects` 안의 폴더를 fzf로 선택하면 tmux 세션을 생성하고 즉시 전환합니다.

- **tmux 단축키:** `Prefix + P`

### ~/.tmux-sessionizer.sh — 프로젝트 세션 관리자

`~/project`, `~/work` 경로에서 프로젝트를 선택하면 nvim(70%) + claude(30%) 레이아웃으로 자동 구성합니다. 동일 프로젝트 내 여러 작업 세션(fix, feature 등)도 지원합니다.

- **tmux 단축키:** `Prefix + F`

### ~/.claude-skills.sh — Claude Code 스킬 팝업 메뉴

현재 tmux 세션에서 실행 중인 Claude Code 패널을 자동으로 찾아 프롬프트를 전송합니다.

- **tmux 단축키:** `Prefix + C`

```bash
# 스킬 목록은 "이름 | 프롬프트" 형식으로 추가
SKILLS="
🔍 프로젝트 요약 | 현재 프로젝트의 전체 구조와 핵심 로직을 분석해서 요약해 줘.
🐛 코드 리뷰 | 방금 작성한 코드에서 개선할 점이나 잠재적인 버그가 있는지 확인해 줘.
📝 리팩토링 | 이 코드를 더 읽기 쉽고 효율적으로 리팩토링해 주고 이유를 설명해 줘.
"
```

---

## Phase 5. 실전 바이브 코딩 워크플로우

1. **디렉토리 이동 (zoxide):** `cd 프로젝트명`으로 스마트 이동
2. **Git UI (lazygit):** `lg` 단축어로 실행
3. **도구 런처:** `tools` 입력 후 fzf로 btop, lazygit, duf, dust, fastfetch 선택 실행
4. **바이브 코딩 시작 (tmux):**
   - `tmux` 입력
   - `Ctrl+b` 후 `"` 또는 `%`로 화면 분할
   - 위쪽에 `nvim`, 아래쪽에 `claude` 실행
5. **프롬프트 전송:**
   - Neovim에서 `v`로 블록 지정 → **Space + s** → Enter로 Claude로 전송
   - Claude가 파일 작성을 마치면 Neovim에서 확인
6. **Claude 스킬 호출:** `Prefix + C` → 스킬 선택 → Claude 패널로 자동 전송

---

## 설치된 도구 목록

| 도구 | 설명 |
|------|------|
| `bat` | cat 대체, 구문 강조 |
| `btop` | 시스템 모니터 |
| `duf` | 디스크 사용량 |
| `dust` | 폴더 크기 분석 |
| `fastfetch` | 시스템 정보 표시 |
| `fd` | find 대체 |
| `fzf` | 퍼지 파인더 |
| `git-delta` | git diff 뷰어 |
| `lazygit` | Git TUI |
| `lsd` | ls 대체, 아이콘 포함 |
| `mise` | 런타임 버전 관리 |
| `navi` | 명령어 치트시트 |
| `neovim` | 에디터 |
| `ripgrep` | grep 대체 |
| `starship` | 프롬프트 |
| `tmux` | 터미널 멀티플렉서 |
| `zoxide` | 스마트 cd |
| `claude` | Claude Code CLI (네이티브) |
| `gemini` | Gemini CLI |
