#!/bin/bash
# para-work.sh — PARA 개인 작업 통합 헬퍼 스크립트
#
# 사용법:
#   para-work backup      Obsidian 볼트 수동 백업 (DOC: backup YYYY-MM-DD HH:mm:ss)
#   para-work briefing    NEXT-SESSION.md 브리핑 조회 및 갱신 헬퍼
#   para-work notion      Notion 루틴(다이어리/식단/예산) SOP 열람
#   para-work menu        fzf 인터랙티브 메뉴 (인자 생략 시 기본값)

set -euo pipefail

PARA_DIR="$HOME/Project/para"
NEXT_SESSION_FILE="$PARA_DIR/NEXT-SESSION.md"
NOTION_OPS_DIR="$PARA_DIR/02.Areas/07.개인관리"

_now_timestamp() {
    date '+%Y-%m-%d %H:%M:%S'
}

_today_date() {
    date '+%Y-%m-%d'
}

# 1. Vault Backup
do_backup() {
    echo "📦 PARA 볼트 백업 시작: $PARA_DIR"
    if [ ! -d "$PARA_DIR" ]; then
        echo "❌ 오류: PARA 볼트 디렉토리를 찾을 수 없습니다 ($PARA_DIR)" >&2
        exit 1
    fi
    
    cd "$PARA_DIR"
    git add .
    local ts
    ts=$(_now_timestamp)
    git commit -m "DOC: backup $ts" || {
        echo "ℹ️ 커밋할 변경 사항이 없습니다."
        return 0
    }
    git push || {
        echo "⚠️ git push 실패. 네트워크 연결 또는 원격 설정을 확인하세요." >&2
        return 1
    }
    echo "✅ PARA 볼트 백업 완료! ($ts)"
}

# 2. Briefing Check & Update
do_briefing() {
    if [ ! -f "$NEXT_SESSION_FILE" ]; then
        echo "❌ 오류: NEXT-SESSION.md 파일을 찾을 수 없습니다 ($NEXT_SESSION_FILE)" >&2
        exit 1
    fi

    echo "📋 [NEXT-SESSION.md 브리핑]"
    echo "--------------------------------------------------------"
    head -n 25 "$NEXT_SESSION_FILE"
    echo "--------------------------------------------------------"
    
    echo "💡 옵션을 선택하세요:"
    echo "1) 전체 파일 열람"
    echo "2) 최종 갱신일 오늘 날짜($(_today_date))로 업데이트"
    echo "3) 돌아가기"
    read -rp "선택 (1/2/3): " choice

    case "$choice" in
        1)
            if command -v nvim >/dev/null 2>&1; then
                nvim "$NEXT_SESSION_FILE"
            else
                less "$NEXT_SESSION_FILE"
            fi
            ;;
        2)
            local today
            today=$(_today_date)
            sed -i '' "s/최종 갱신: [0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/최종 갱신: $today/" "$NEXT_SESSION_FILE" 2>/dev/null || \
            sed -i "s/최종 갱신: [0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/최종 갱신: $today/" "$NEXT_SESSION_FILE"
            echo "✅ 최종 갱신일이 $today 로 업데이트되었습니다."
            ;;
        *)
            echo "취소되었습니다."
            ;;
    esac
}

# 3. Notion Ops SOP Viewer
do_notion() {
    if [ ! -d "$NOTION_OPS_DIR" ]; then
        echo "❌ 오류: 개인관리 디렉토리를 찾을 수 없습니다 ($NOTION_OPS_DIR)" >&2
        exit 1
    fi

    local selected
    if command -v fzf >/dev/null 2>&1; then
        selected=$(find "$NOTION_OPS_DIR" -name "*.md" | fzf --prompt="🍱 Notion SOP 선택 > " --height=40% --reverse --border=rounded)
    else
        echo "Notion SOP 목록:"
        find "$NOTION_OPS_DIR" -name "*.md"
        read -rp "열람할 파일 경로 입력: " selected
    fi

    if [ -n "$selected" ] && [ -f "$selected" ]; then
        if command -v nvim >/dev/null 2>&1; then
            nvim "$selected"
        else
            less "$selected"
        fi
    fi
}

# 4. Interactive Menu
do_menu() {
    local options=(
        "📦 PARA 볼트 백업 (git commit & push) | backup"
        "📋 NEXT-SESSION 브리핑 열람/갱신 | briefing"
        "🍱 Notion 루틴 SOP (일기·식단·예산) 열람 | notion"
        "❌ 종료 | exit"
    )

    local choice
    if command -v fzf >/dev/null 2>&1; then
        choice=$(printf '%s\n' "${options[@]}" | fzf --prompt="🚀 개인 작업 선택 > " --height=40% --layout=reverse --border=rounded)
    else
        echo "🚀 실행할 작업을 선택하세요:"
        for i in "${!options[@]}"; do
            echo "$((i+1))) ${options[$i]}"
        done
        read -rp "선택 번호: " num
        choice="${options[$((num-1))]:-}"
    fi

    local action
    action=$(echo "$choice" | awk -F ' \\| ' '{print $2}')

    case "$action" in
        backup)   do_backup ;;
        briefing) do_briefing ;;
        notion)   do_notion ;;
        exit|"")  exit 0 ;;
        *)        echo "알 수 없는 작업입니다: $action" ;;
    esac
}

# Subcommand Router
CMD="${1:-menu}"

case "$CMD" in
    backup)   do_backup ;;
    briefing) do_briefing ;;
    notion)   do_notion ;;
    menu)     do_menu ;;
    *)
        echo "사용법: para-work [backup|briefing|notion|menu]"
        exit 1
        ;;
esac
