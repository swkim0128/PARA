# 이메일 분류 자동화처리 설계 문서

## 1. 시스템 개요

### 1.1 목표
Gmail 이메일을 AI를 활용하여 자동으로 분석하고 적절한 라벨을 할당하여 체계적으로 관리

### 1.2 전체 아키텍처
```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌─────────┐
│  Gmail  │────▶│ n8n      │────▶│   AI     │────▶│  분류    │────▶│ Gmail   │
│  수신함  │     │ Trigger  │     │  분석    │     │  로직    │     │ 라벨링  │
└─────────┘     └──────────┘     └──────────┘     └──────────┘     └─────────┘
```

## 2. 주요 컴포넌트

### 2.1 n8n 워크플로우

#### 워크플로우 1: 기존 이메일 일괄 처리
```
[Gmail Node: List Messages]
    ↓
[Loop: For Each Email]
    ↓
[Gmail Node: Get Message Details]
    ↓
[AI Node: Analyze Content]
    ↓
[Function Node: Determine Label]
    ↓
[Gmail Node: Modify Labels]
```

#### 워크플로우 2: 실시간 이메일 처리
```
[Webhook/Trigger: New Email]
    ↓
[Gmail Node: Get Message Details]
    ↓
[AI Node: Analyze Content]
    ↓
[Function Node: Determine Label]
    ↓
[Gmail Node: Modify Labels]
    ↓
[Optional: Send Notification]
```

### 2.2 Gmail API 연동

#### 필요 권한
- `gmail.readonly`: 이메일 읽기
- `gmail.modify`: 라벨 수정
- `gmail.labels`: 라벨 관리

#### 주요 API 엔드포인트
```javascript
// 이메일 목록 조회
GET https://gmail.googleapis.com/gmail/v1/users/me/messages

// 이메일 상세 조회
GET https://gmail.googleapis.com/gmail/v1/users/me/messages/{messageId}

// 라벨 수정
POST https://gmail.googleapis.com/gmail/v1/users/me/messages/{messageId}/modify

// 라벨 목록 조회
GET https://gmail.googleapis.com/gmail/v1/users/me/labels
```

### 2.3 AI 분석 로직

#### 프롬프트 구조
```
당신은 이메일을 분석하여 적절한 카테고리로 분류하는 AI 어시스턴트입니다.

다음 이메일을 분석하고 가장 적합한 카테고리를 선택해주세요:

**이메일 정보:**
- 발신자: {sender}
- 제목: {subject}
- 본문: {body}

**카테고리 목록:**
1. 업무/회사
2. 프로모션/광고
3. 소셜/SNS
4. 금융/결제
5. 쇼핑/구매
6. 개인/기타
7. 중요/긴급

**출력 형식:**
카테고리: [선택된 카테고리]
신뢰도: [0-100]
이유: [간단한 설명]
```

#### 응답 파싱
```javascript
// AI 응답 예시
{
  "category": "업무/회사",
  "confidence": 95,
  "reason": "회사 이메일 주소에서 발송되었으며, 업무 관련 키워드가 포함됨"
}
```

## 3. 데이터 모델

### 3.1 이메일 데이터 구조
```javascript
{
  id: "message_id",
  threadId: "thread_id",
  sender: {
    email: "sender@example.com",
    name: "Sender Name"
  },
  subject: "Email Subject",
  body: "Email Body Content",
  receivedAt: "2025-12-12T10:00:00Z",
  labels: ["INBOX", "UNREAD"]
}
```

### 3.2 분류 결과 구조
```javascript
{
  messageId: "message_id",
  category: "업무/회사",
  confidence: 95,
  suggestedLabel: "Work",
  processedAt: "2025-12-12T10:05:00Z"
}
```

## 4. 라벨 매핑

### 4.1 카테고리 → Gmail 라벨
```javascript
const labelMapping = {
  "업무/회사": "Work",
  "프로모션/광고": "Promotions",
  "소셜/SNS": "Social",
  "금융/결제": "Finance",
  "쇼핑/구매": "Shopping",
  "개인/기타": "Personal",
  "중요/긴급": "Important"
};
```

### 4.2 라벨 생성 규칙
- 라벨이 없으면 자동 생성
- 색상 코드 자동 할당
- 부모/자식 라벨 구조 지원

## 5. 워크플로우 상세

### 5.1 기존 이메일 일괄 처리

```javascript
// n8n 노드 설정

// 1. Gmail: List Messages
{
  maxResults: 100,
  q: "is:unread" // 읽지 않은 이메일만
}

// 2. Loop: For Each
{
  batchSize: 10 // 한 번에 10개씩 처리
}

// 3. Gmail: Get Message
{
  format: "full",
  metadataHeaders: ["From", "Subject", "Date"]
}

// 4. Function: Extract Email Data
return {
  sender: items[0].json.payload.headers.find(h => h.name === 'From').value,
  subject: items[0].json.payload.headers.find(h => h.name === 'Subject').value,
  body: items[0].json.snippet
};

// 5. HTTP Request: Claude API
{
  method: "POST",
  url: "https://api.anthropic.com/v1/messages",
  body: {
    model: "claude-sonnet-4-20250514",
    messages: [{
      role: "user",
      content: `이메일 분류 프롬프트...`
    }]
  }
}

// 6. Function: Parse AI Response
// JSON 파싱 및 라벨 결정

// 7. Gmail: Modify Labels
{
  addLabelIds: [determinedLabelId],
  removeLabelIds: ["UNREAD"]
}
```

### 5.2 실시간 처리 트리거

**옵션 1: Gmail Webhook (Push Notification)**
```javascript
// Google Cloud Pub/Sub 설정
{
  topic: "projects/YOUR_PROJECT/topics/gmail-notifications",
  subscription: "gmail-subscription"
}
```

**옵션 2: 스케줄 기반 폴링**
```javascript
// n8n Cron 노드
{
  expression: "*/5 * * * *" // 5분마다 실행
}
```

## 6. 에러 핸들링

### 6.1 재시도 로직
```javascript
{
  maxRetries: 3,
  retryDelay: 5000, // 5초
  retryOn: ["RATE_LIMIT", "NETWORK_ERROR"]
}
```

### 6.2 에러 로깅
```javascript
// 에러 발생 시 로그 저장
{
  messageId: "xxx",
  error: {
    type: "API_ERROR",
    message: "Rate limit exceeded",
    timestamp: "2025-12-12T10:00:00Z"
  }
}
```

### 6.3 폴백 로직
- AI 분석 실패 시 → 기본 규칙 기반 분류
- API 호출 실패 시 → 큐에 저장 후 재시도
- 라벨 적용 실패 시 → 에러 로그 기록

## 7. 성능 최적화

### 7.1 배치 처리
- 한 번에 10-20개 이메일씩 처리
- API 호출 최소화

### 7.2 캐싱
```javascript
// 발신자별 분류 결과 캐싱
const senderCache = {
  "sender@example.com": {
    category: "업무/회사",
    lastUpdated: "2025-12-12T10:00:00Z"
  }
};
```

### 7.3 Rate Limiting
```javascript
// API 호출 제한
{
  maxRequestsPerMinute: 60,
  maxConcurrent: 5
}
```

## 8. 테스트 계획

### 8.1 단위 테스트
- AI 프롬프트 테스트
- 라벨 매핑 테스트
- 에러 핸들링 테스트

### 8.2 통합 테스트
- 전체 워크플로우 테스트
- 다양한 이메일 타입 테스트

### 8.3 성능 테스트
- 대량 이메일 처리 테스트 (1000+ 이메일)
- 응답 시간 측정

## 9. 배포 및 모니터링

### 9.1 배포 체크리스트
- [ ] n8n 로컬 실행 확인
- [ ] Gmail API 인증 완료
- [ ] AI API 키 설정
- [ ] 워크플로우 임포트
- [ ] 테스트 실행
- [ ] 실제 이메일로 검증

### 9.2 모니터링 지표
- 처리된 이메일 수
- 분류 정확도
- API 응답 시간
- 에러 발생 빈도

## 10. 향후 개선 사항

### 10.1 기능 추가
- [ ] 사용자 피드백 기반 학습
- [ ] 복잡한 라벨 규칙 (AND/OR 조건)
- [ ] 이메일 우선순위 자동 설정
- [ ] 스팸 필터링 강화

### 10.2 성능 개선
- [ ] 병렬 처리 최적화
- [ ] 캐싱 전략 고도화
- [ ] AI 모델 파인튜닝

### 10.3 사용성 개선
- [ ] 웹 대시보드 개발
- [ ] 분류 규칙 GUI 설정
- [ ] 통계 및 리포트 기능
