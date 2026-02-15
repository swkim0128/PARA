#!/bin/bash

# ==============================================================================
# [ 스크립트 명 ] : Google Drive Docs to Obsidian Markdown Converter
# [ 작성 목적 ] : NotebookLM에서 생성된 Google 문서를 마크다운(.md)으로 변환하여
#                로컬 옵시디언 보관함으로 동기화하고, 원본을 정리합니다.
#
# [ 필수 요구 사항 ] :
#   1. rclone 설치: `brew install rclone`
#   2. rclone 설정: `rclone config`를 통해 'gdrive'라는 이름의 원격 저장소 설정 완료
#
# [ 주요 기능 ] :
#   - Google Docs 파일을 Markdown(.md) 포맷으로 자동 변환하여 다운로드
#   - 동기화 완료 후 Mac 시스템 알림 전송
#   - 로컬 이동이 완료된 Google Drive 원본 파일 자동 삭제 (move)
#
# [ 실행 방법 ] :
#   - 수동 실행: 터미널에서 `sync_gdrive.sh` 입력 (PATH 설정 시)
#   - 자동 실행: crontab 등을 이용한 스케줄링 등록 가능
# ==============================================================================

# --- 설정 구간 ---
# rclone 설정 시 정한 이름
REMOTE_NAME="gdrive"
# 구글 드라이브 내 소스 폴더 경로 (공백 시 루트)
GDRIVE_SOURCE_DIR="03.Resources/NotebookLM_Exports"
# 로컬 옵시디언 보관함 경로
OBSIDIAN_DEST_DIR="/Users/eunsol/Project/para/gdrive"
# ----------------

echo "🔄 [$(date +'%Y-%m-%d %H:%M:%S')] 동기화 및 마크다운 변환 시작..."

# --drive-export-formats md: 구글 문서를 .md 파일로 내보내기
# -u: 업데이트된 파일만 복사 (Update)
# -v: 진행 상황 상세 출력 (Verbose)
rclone move "${REMOTE_NAME}:${GDRIVE_SOURCE_DIR}" "${OBSIDIAN_DEST_DIR}" \
    --drive-export-formats md \
    -v \
    --progress

# 작업 결과 확인 및 알림 발송
if [ $? -eq 0 ]; then
    echo "✅ 모든 작업이 성공적으로 완료되었습니다."

    # macOS 시스템 알림 발송
    osascript -e 'display notification "모든 구글 문서가 마크다운으로 변환되어 옵시디언에 저장되고 원본이 정리되었습니다." with title "코딩 파트너 동기화" subtitle "작업 완료 🚀"'
else
    echo "❌ 오류가 발생했습니다. 로그를 확인해 주세요."
    osascript -e 'display notification "동기화 중 오류가 발생했습니다. 터미널을 확인하세요." with title "코딩 파트너 동기화" subtitle "작업 실패 ⚠️"'
fi

echo "------------------------------------------------------------------------------"
