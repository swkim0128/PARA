#!/bin/bash

SKILLS_FILE="$HOME/.claude-skills.txt"

# ---------------------------------------------------------
# [1] 스킬 목록 파일 존재 여부 확인
# ---------------------------------------------------------
if [ ! -f "$SKILLS_FILE" ]; then
    tmux display-message "❌ 스킬 목록 파일이 없습니다: $SKILLS_FILE"
    exit 1
fi

# ---------------------------------------------------------
# [2] 클로드 코드가 실행 중인 패널 자동 찾기
# ---------------------------------------------------------
TARGET_PANE=""

for info in $(tmux list-panes -F "#{pane_id},#{pane_tty}"); do
    PANE_ID="${info%,*}"
    PANE_TTY="${info#*,}"

    if ps -t "$PANE_TTY" | grep -iq "[c]laude"; then
        TARGET_PANE="$PANE_ID"
        break
    fi
done

if [ -z "$TARGET_PANE" ]; then
    tmux display-message "❌ 클로드 코드가 실행 중인 패널을 찾을 수 없습니다!"
    exit 1
fi

# ---------------------------------------------------------
# [3] 파일에서 주석/빈 줄 제거 후 fzf로 스킬 선택
# ---------------------------------------------------------
SELECTED=$(grep -v '^\s*#' "$SKILLS_FILE" | grep -v '^\s*$' | fzf \
  --prompt="🤖 클로드 스킬 선택 > " \
  --height=100% --layout=reverse --border=rounded)

if [ -z "$SELECTED" ]; then
    exit 0
fi

# ---------------------------------------------------------
# [4] '|' 뒤의 프롬프트를 추출하여 Claude 패널로 전송
# ---------------------------------------------------------
PROMPT=$(echo "$SELECTED" | awk -F '|' '{print $2}' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

tmux send-keys -l -t "$TARGET_PANE" "$PROMPT"
tmux send-keys -t "$TARGET_PANE" C-m
