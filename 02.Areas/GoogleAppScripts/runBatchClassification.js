function runBatchClassification() {
  // =================================================================
  // [설정] 라벨 매핑 (Gmail 라벨명과 정확히 일치해야 함)
  // =================================================================
  const LABELS = {
    ACTION:   "00.Actions/01.Action",
    READ:     "00.Actions/03.to_read",
    FINANCE:  "02.Areas/재무",
    SECURITY: "02.Areas/계정관리",
    DEV:      "03.Resources/개발",
    HOBBY:    "03.Resources/취미",
    NOTICE:   "04.Archives/서비스 공지"
  };

  var labelMap = {};
  for (var key in LABELS) {
    var label = GmailApp.getUserLabelByName(LABELS[key]);
    if (!label) Logger.log("⚠️ 경고: '" + LABELS[key] + "' 라벨이 없습니다.");
    labelMap[key] = label;
  }

  // =================================================================
  // [실행] 수신함 스캔 (처리량 대폭 증가: 200개)
  // =================================================================
  // 과거 메일도 처리하기 위해 탐색 범위를 늘렸습니다.
  var threads = GmailApp.getInboxThreads(0, 200);
  
  if (threads.length === 0) {
    Logger.log("✅ 수신함이 깨끗합니다 (Inbox Zero).");
    return;
  }

  Logger.log("🔍 " + threads.length + "개의 스레드 정밀 분석 중...");

  for (var i = 0; i < threads.length; i++) {
    var thread = threads[i];
    var msg = thread.getMessages()[0];
    
    // 데이터 전처리 (공백 제거 및 소문자 변환으로 매칭률 극대화)
    var subject = thread.getFirstMessageSubject().toLowerCase().replace(/\s/g, ""); 
    var sender = msg.getFrom().toLowerCase();
    var body = msg.getPlainBody().substring(0, 800).toLowerCase(); 

    var targetLabel = null;
    var logCategory = "";

    // -----------------------------------------------------------------
    // [규칙 1] ⚡️ Action (계정 삭제 경고, 구독 취소, 파일 삭제) - 최우선
    // -----------------------------------------------------------------
    if (matches(subject, ["계정삭제", "accountwillbedeleted", "파일이삭제", "휴지통", "cancelled", "subscriptioncancelled", "비상소집", "마감임박", "d-day"])) {
      targetLabel = labelMap.ACTION;
      logCategory = "⚡️ [Action/경고]";
    }

    // -----------------------------------------------------------------
    // [규칙 2] 💰 재무/쇼핑 (견적서, 가상화폐, 결제)
    // -----------------------------------------------------------------
    else if (matches(subject, ["견적", "온라인견적", "priceprotection", "trade", "주문", "결제", "영수증", "invoice", "receipt", "환불", "적립금", "최선집행"]) || 
             matches(sender, ["danawa", "착한컴", "binance", "toss", "tossinvest", "naverpay", "pay", "bananamall", "xd-design"])) {
      targetLabel = labelMap.FINANCE;
      logCategory = "💰 [재무/쇼핑]";
    }

    // -----------------------------------------------------------------
    // [규칙 3] 💻 커리어/개발 (입사지원, 코딩테스트, 채용)
    // -----------------------------------------------------------------
    else if (matches(subject, ["지원서", "채용", "서류", "합격", "불합격", "코딩테스트", "면접", "입사", "recruiting", "bug", "버그", "version", "release"]) || 
             matches(sender, ["iportfolio", "wanted", "programmers", "ssafy", "multicampus", "routinery", "github", "vercel", "jetbrains"])) {
      targetLabel = labelMap.DEV;
      logCategory = "💻 [커리어/개발]";
    }

    // -----------------------------------------------------------------
    // [규칙 4] 🔐 보안/계정 (로그인, 인증)
    // -----------------------------------------------------------------
    else if (matches(subject, ["로그인", "보안", "인증", "verification", "code", "sign-in", "security"]) ||
             matches(sender, ["verify", "auth", "noreply", "member"])) {
      targetLabel = labelMap.SECURITY;
      logCategory = "🔐 [계정/보안]";
    }

    // -----------------------------------------------------------------
    // [규칙 5] ☕️ 읽을거리 (YBM, 뉴스레터, 브랜드 홍보)
    // -----------------------------------------------------------------
    else if (matches(subject, ["뉴스레터", "영어", "토익", "학습", "launch", "release", "출시", "도착했습니다", "컬러포커스"]) || 
             matches(sender, ["ybm", "ybmnet", "montblanc", "microsoft", "windowsinsider", "lifecoloring", "publy", "jiran"])) {
      targetLabel = labelMap.READ;
      logCategory = "☕️ [읽을거리]";
    }

    // -----------------------------------------------------------------
    // [규칙 6] 📜 단순 공지 (약관, 개인정보)
    // -----------------------------------------------------------------
    else if (matches(subject, ["약관", "개정", "개인정보", "수집출처", "policy", "terms", "notice", "공지"])) {
      targetLabel = labelMap.NOTICE;
      logCategory = "📜 [공지]";
    }

    // -----------------------------------------------------------------
    // [적용]
    // -----------------------------------------------------------------
    if (targetLabel) {
      thread.addLabel(targetLabel);
      thread.moveToArchive();
      Logger.log(logCategory + " : " + thread.getFirstMessageSubject());
    } else {
      Logger.log("❓ [미분류] : " + thread.getFirstMessageSubject());
    }
  }
  
  // [추가] 실행 완료 후 터미널에 전달할 메시지 반환
  return "Successfully processed " + threads.length + " threads.";
}

// 헬퍼 함수
function matches(text, keywords) {
  if (!text) return false;
  for (var i = 0; i < keywords.length; i++) {
    if (text.includes(keywords[i])) return true;
  }
  return false;
}

// 외부(터미널)에서 호출을 받기 위한 접점
function doGet() {
  try {
    var result = runBatchClassification();
    return ContentService.createTextOutput(result); // "Successfully processed..." 출력
  } catch (err) {
    return ContentService.createTextOutput("Error: " + err.toString());
  }
}