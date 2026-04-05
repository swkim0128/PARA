#!/bin/bash
# ~/Projects 디렉토리 안의 폴더 목록을 fzf로 띄움
SELECTED=$(find ~/Projects -mindepth 1 -maxdepth 1 -type d | fzf --prompt="📂 프로젝트 이동 > " --height=40% --layout=reverse --border=rounded)

if [ -z "$SELECTED" ]; then
    exit 0
fi

# 폴더 이름만 추출해서 세션 이름으로 사용
SESSION_NAME=$(basename "$SELECTED" | tr . _)

# 해당 세션이 없으면 백그라운드에서 새로 생성
if ! tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    tmux new-session -d -s "$SESSION_NAME" -c "$SELECTED"
fi

# 선택한 세션으로 즉시 전환
tmux switch-client -t "$SESSION_NAME"
