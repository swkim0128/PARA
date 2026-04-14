#!/bin/bash

PATHS_FILE="$HOME/.project-paths.txt"

# ---------------------------------------------------------
# [1] 경로 목록 파일 존재 여부 확인
# ---------------------------------------------------------
if [ ! -f "$PATHS_FILE" ]; then
    echo -e "\033[0;31m[오류]\033[0m 경로 목록 파일이 없습니다: $PATHS_FILE"
    exit 1
fi

# ---------------------------------------------------------
# [2] 파일에서 경로 읽기 (주석/빈 줄 제외)
# ---------------------------------------------------------
mapfile -t paths < <(grep -v '^\s*#' "$PATHS_FILE" | grep -v '^\s*$' | sed "s|~|$HOME|g")

# ---------------------------------------------------------
# [3] fzf로 프로젝트 폴더 선택
# ---------------------------------------------------------
SELECTED=$(find "${paths[@]}" -mindepth 1 -maxdepth 1 -type d 2>/dev/null \
  | fzf --prompt="📂 프로젝트 이동 > " --height=40% --layout=reverse --border=rounded)

if [ -z "$SELECTED" ]; then
    exit 0
fi

# ---------------------------------------------------------
# [4] 세션 생성 및 전환
# ---------------------------------------------------------
SESSION_NAME=$(basename "$SELECTED" | tr . _)

if ! tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    tmux new-session -d -s "$SESSION_NAME" -c "$SELECTED"
fi

tmux switch-client -t "$SESSION_NAME"
