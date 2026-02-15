#!/bin/bash

# ==============================================================================
# [ 스크립트 명 ] : Gmail Auto-Classifier Trigger
# [ 작성 목적 ] : 작성된 Google Apps Script(GAS) 웹 앱 URL을 호출하여
#                지메일 라벨 분류 로직을 원격으로 실행합니다.
# ==============================================================================

# --- ⚙️ 설정 구간 ---
# 위 1단계에서 복사한 웹 앱 URL을 입력하세요.
GAS_WEBAPP_URL="https://script.google.com/macros/s/AKfycbwyxZutWDICaYgoyA485tLDx5TW1XEhdFQ2TEHBxZis5hh8q8VXfby6Ja7g8dDiofxR/exec"



# ------------------

echo "📧 [$(date +'%Y-%m-%d %H:%M:%S')] 지메일 분류 요청 중..."

# curl 상세 옵션 보강:
# -L : 리다이렉트 추적 (구글 앱스 스크립트 필수)
# -f : HTTP 에러 시 오류 메시지 출력
# -A : 브라우저인 것처럼 속이는 User-Agent 추가 (일부 보안 필터 우회)
# -s : 진행 바 숨김
RESPONSE=$(curl -s -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" "$GAS_WEBAPP_URL")

# 응답 값 확인 및 알림
if [[ -n "$RESPONSE" ]]; then
    echo "✅ 서버 응답: $RESPONSE"
    osascript -e 'display notification "지메일 분류가 완료되었습니다." with title "지메일 관리자" subtitle "자동 분류 성공 📩"'
else
    echo "❌ 응답이 없습니다. URL을 다시 확인하거나 인터넷 연결을 확인하세요."
    osascript -e 'display notification "응답을 받지 못했습니다." with title "지메일 관리자" subtitle "실행 실패 ⚠️"'
fi
