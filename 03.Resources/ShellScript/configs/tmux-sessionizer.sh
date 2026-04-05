#!/bin/bash

# 1. 프로젝트 경로 설정
paths=(~/project ~/work)

# 2. fzf로 폴더 선택
selected=$(find "${paths[@]}" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | fzf --prompt="📂 프로젝트 선택 > " --height=100% --layout=reverse --border=rounded)

if [[ -z $selected ]]; then
    exit 0
fi

base_name=$(basename "$selected" | tr . _)

# 3. 동일 프로젝트 내 여러 작업 처리를 위한 분기
# 이미 해당 프로젝트의 기본 세션이 있는지 확인
existing_sessions=$(tmux list-sessions -F "#S" | grep "^${base_name}" | tr '\n' ' ')

if [[ -n $existing_sessions ]]; then
    # 기존 세션 목록을 보여주고, 'New Task' 옵션을 추가
    target=$(echo -e "🆕 [New Task Session]\n${existing_sessions// /\\n}" | grep -v '^$' | fzf --prompt="🎯 접속할 세션 선택 (또는 새 작업 생성) > " --height=40% --layout=reverse --border=rounded)

    if [[ -z $target ]]; then exit 0; fi

    # 'New Task'를 선택했다면 작업 접미사(Suffix)를 입력받음
    if [[ "$target" == "🆕 [New Task Session]" ]]; then
        # 팝업 형태의 read를 위해 tmux command 사용
        task_name=$(tmux command-prompt -p "작업 명칭을 입력하세요 (예: fix, feature, refactor):" "run-shell 'echo %%'")
        # 취소했거나 빈값이면 기본 이름 사용, 값이 있으면 접미사 추가
        if [[ -n $task_name ]]; then
            session_name="${base_name}:${task_name}"
        else
            session_name="${base_name}_$(date +%H%M%S)" # 이름 중복 방지를 위해 시간초 사용
        fi
    else
        session_name="$target"
    fi
else
    session_name="$base_name"
fi

# 4. 세션 생성 및 전환 로직
if ! tmux has-session -t "$session_name" 2>/dev/null; then
    # 새 세션 생성 시 레이아웃 자동 구성 (Nvim 70%, Claude 30%)
    tmux new-session -d -s "$session_name" -c "$selected"
    tmux send-keys -t "$session_name" "nvim ." C-m
    tmux split-window -h -p 30 -t "$session_name" -c "$selected"
    tmux send-keys -t "$session_name" "claude" C-m
    tmux select-pane -t 1
fi

if [[ -z $TMUX ]]; then
    tmux attach-session -t "$session_name"
else
    tmux switch-client -t "$session_name"
fi
