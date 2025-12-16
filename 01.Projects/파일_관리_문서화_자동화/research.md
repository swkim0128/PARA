# 파일 관리 및 문서화 자동화 프로젝트

## 프로젝트 개요

### 목표
맥북 명령어 하나로 일상 작업을 자동으로 문서화하는 시스템 구축

### 핵심 요구사항
1. 작업 내용을 간단한 명령어로 기록
2. 자동으로 구조화된 문서 생성
3. 파일 자동 정리 및 분류
4. 노션 또는 마크다운으로 문서 저장

---

## 조사: 자동화 방법 비교

### 방법 1: Shell Script + Git

#### 개요
작업을 Git 커밋으로 기록하고, 커밋 히스토리를 문서화

#### 구현 방법
```bash
# 작업 기록 명령어
work-log "프로젝트 설정 완료"

# 내부 동작
# 1. 작업 내용을 커밋 메시지로 저장
# 2. Git log를 파싱하여 문서 생성
# 3. Markdown 파일로 내보내기
```

#### 장점
✅ Git 기본 기능 활용
✅ 버전 관리와 문서화 통합
✅ 커밋 히스토리 = 작업 이력
✅ 추가 도구 불필요

#### 단점
❌ Git 리포지토리 필요
❌ 복잡한 구조화 어려움
❌ 실시간 문서 업데이트 제한적

#### 평가
⭐⭐⭐☆☆ (3/5)
간단한 작업 로그에는 적합하나, 구조화된 문서 생성에는 한계

---

### 방법 2: macOS Automator

#### 개요
macOS 기본 자동화 도구로 GUI 기반 워크플로우 생성

#### 구현 방법
1. Quick Action 생성
2. AppleScript로 작업 로그 수집
3. TextEdit 또는 Notes 앱에 자동 기록

#### 장점
✅ macOS 기본 도구 (설치 불필요)
✅ GUI 기반으로 쉬운 설정
✅ 다양한 앱 연동 가능
✅ 단축키 할당 가능

#### 단점
❌ 복잡한 로직 구현 어려움
❌ 버전 관리 어려움
❌ 유연성 부족
❌ CLI 기반 사용 제한적

#### 평가
⭐⭐☆☆☆ (2/5)
간단한 자동화에는 적합하나, 복잡한 문서화에는 부적합

---

### 방법 3: Alfred Workflows

#### 개요
Alfred 앱의 Workflow 기능으로 키워드 기반 자동화

#### 구현 방법
```
키워드 입력: work 프로젝트 설정 완료
↓
Python/Shell 스크립트 실행
↓
데이터 수집 → 문서 생성 → 노션 업로드
```

#### 장점
✅ 빠른 호출 (키워드)
✅ Python/Shell 스크립트 통합
✅ 클립보드 활용 편리
✅ 시각적 피드백

#### 단점
❌ Alfred Powerpack 필요 (유료)
❌ macOS 전용
❌ 학습 곡선 존재

#### 평가
⭐⭐⭐⭐☆ (4/5)
강력하고 유연하나 유료 라이선스 필요

---

### 방법 4: Python CLI 도구 ⭐ 추천

#### 개요
Python으로 커스텀 CLI 도구를 만들어 완벽히 제어

#### 구현 방법
```bash
# 설치
pip install work-logger

# 사용
work-log add "프로젝트 설정 완료" --category setup
work-log doc --output notion
work-log doc --output markdown
```

#### 구조
```python
# work_logger/
├── cli.py          # CLI 인터페이스 (Click/Typer)
├── logger.py       # 작업 로그 수집
├── formatter.py    # 문서 포맷팅
├── exporters/
│   ├── notion.py   # 노션 내보내기
│   ├── markdown.py # 마크다운 내보내기
│   └── pdf.py      # PDF 내보내기
└── config.py       # 설정 관리
```

#### 장점
✅ **완전한 커스터마이징**
✅ 모든 기능 직접 구현 가능
✅ CLI로 빠른 사용
✅ 노션 API 연동 가능
✅ 확장 가능한 구조
✅ 크로스 플랫폼

#### 단점
❌ 초기 개발 시간 필요
❌ Python 지식 필요

#### 평가
⭐⭐⭐⭐⭐ (5/5)
**최적의 솔루션** - 유연성, 확장성, 제어 가능성 모두 우수

---

### 방법 5: Obsidian + Templater

#### 개요
Obsidian 메모 앱의 Templater 플러그인으로 자동화

#### 구현 방법
1. Daily Note 템플릿 생성
2. Templater로 자동 데이터 입력
3. Dataview로 작업 로그 쿼리

#### 장점
✅ 마크다운 기반 관리
✅ 강력한 링크 시스템
✅ 로컬 파일 저장
✅ 플러그인 생태계 풍부

#### 단점
❌ Obsidian 앱 필요
❌ CLI 사용 제한적
❌ 외부 연동 어려움

#### 평가
⭐⭐⭐☆☆ (3/5)
마크다운 위주 관리에는 좋으나, CLI 자동화에는 부적합

---

### 방법 6: Notion API + CLI

#### 개요
Notion API를 직접 호출하여 페이지 생성 및 업데이트

#### 구현 방법
```bash
# Shell 함수로 간단히
function work() {
  curl -X POST https://api.notion.com/v1/pages \
    -H "Authorization: Bearer $NOTION_TOKEN" \
    -d "{...}"
}
```

#### 장점
✅ 노션 직접 연동
✅ 구조화된 데이터베이스
✅ 웹 접근 가능
✅ 협업 용이

#### 단점
❌ Notion API 학습 필요
❌ 네트워크 의존
❌ API 제한 존재

#### 평가
⭐⭐⭐⭐☆ (4/5)
노션 사용자에게 최적, Python CLI와 결합 시 최강

---

## 최적 솔루션: Python CLI + Notion API

### 선택 이유
1. **완전한 제어**: 모든 기능 직접 구현
2. **확장성**: 필요에 따라 기능 추가 용이
3. **노션 연동**: 기존 워크플로우와 통합
4. **CLI 편의성**: 터미널에서 빠른 사용
5. **재사용성**: 다른 프로젝트에도 활용

### 구현 계획

#### Phase 1: 기본 CLI 도구 (1주)
```bash
# 기본 명령어
work add "작업 내용"
work list
work today
```

#### Phase 2: 노션 연동 (1주)
```bash
# 노션 내보내기
work sync notion
work doc --today
```

#### Phase 3: 고급 기능 (1주)
```bash
# 카테고리, 태그, 시간 추적
work add "작업" --category dev --tags python,cli
work stats --week
work report --month
```

---

## 구현 가이드

### 1. 프로젝트 구조

```
work-logger/
├── README.md
├── setup.py
├── requirements.txt
├── work_logger/
│   ├── __init__.py
│   ├── cli.py              # CLI 진입점
│   ├── models.py           # 데이터 모델
│   ├── storage.py          # 로컬 저장 (JSON/SQLite)
│   ├── formatters/
│   │   ├── __init__.py
│   │   ├── markdown.py
│   │   └── notion.py
│   ├── exporters/
│   │   ├── __init__.py
│   │   ├── notion_export.py
│   │   └── file_export.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── datetime_utils.py
└── tests/
```

### 2. 기술 스택

**Core**:
- Python 3.9+
- Click or Typer (CLI 프레임워크)
- SQLite or TinyDB (로컬 저장)

**Notion 연동**:
- notion-client (공식 Python SDK)

**문서 생성**:
- python-markdown
- Jinja2 (템플릿)

**날짜/시간**:
- python-dateutil
- pytz

### 3. 설치 및 설정

```bash
# 1. 리포지토리 생성
mkdir work-logger
cd work-logger
python -m venv venv
source venv/bin/activate

# 2. 의존성 설치
pip install click notion-client python-dateutil

# 3. 개발 모드 설치
pip install -e .

# 4. 설정
work config init
work config set notion-token "YOUR_NOTION_TOKEN"
work config set notion-database-id "YOUR_DB_ID"
```

### 4. CLI 명령어 설계

#### 작업 추가
```bash
# 기본
work add "프로젝트 초기 설정 완료"

# 옵션 포함
work add "API 개발 완료" \
  --category development \
  --tags python,api \
  --time 2.5h \
  --project "백엔드 개발"
```

#### 조회
```bash
# 오늘 작업
work list --today

# 이번 주 작업
work list --week

# 특정 날짜
work list --date 2025-12-15

# 프로젝트별
work list --project "백엔드 개발"
```

#### 문서 생성
```bash
# 마크다운으로 내보내기
work doc --output work-log-2025-12.md

# 노션으로 동기화
work sync notion

# 주간 리포트
work report --week --output notion
```

#### 통계
```bash
# 이번 달 통계
work stats --month

# 프로젝트별 시간
work stats --by-project

# 카테고리별 분포
work stats --by-category
```

### 5. 데이터 모델

```python
# models.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class WorkLog:
    id: str
    content: str
    category: str
    tags: List[str]
    project: Optional[str]
    time_spent: Optional[float]  # hours
    created_at: datetime
    
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'category': self.category,
            'tags': self.tags,
            'project': self.project,
            'time_spent': self.time_spent,
            'created_at': self.created_at.isoformat()
        }
```

### 6. 노션 연동 구현

```python
# exporters/notion_export.py
from notion_client import Client

class NotionExporter:
    def __init__(self, token, database_id):
        self.client = Client(auth=token)
        self.database_id = database_id
    
    def create_page(self, work_log: WorkLog):
        """작업 로그를 노션 페이지로 생성"""
        self.client.pages.create(
            parent={"database_id": self.database_id},
            properties={
                "제목": {
                    "title": [{"text": {"content": work_log.content}}]
                },
                "카테고리": {
                    "select": {"name": work_log.category}
                },
                "태그": {
                    "multi_select": [{"name": tag} for tag in work_log.tags]
                },
                "작업 시간": {
                    "number": work_log.time_spent
                },
                "날짜": {
                    "date": {"start": work_log.created_at.isoformat()}
                }
            }
        )
```

### 7. 마크다운 문서 생성

```python
# formatters/markdown.py
from jinja2 import Template

DAILY_TEMPLATE = """
# {{ date }}

## 작업 내역

{% for log in logs %}
### {{ log.created_at.strftime('%H:%M') }} - {{ log.content }}
- **카테고리**: {{ log.category }}
- **태그**: {{ log.tags | join(', ') }}
{% if log.project %}
- **프로젝트**: {{ log.project }}
{% endif %}
{% if log.time_spent %}
- **소요 시간**: {{ log.time_spent }}시간
{% endif %}

{% endfor %}

## 총 작업 시간
{{ total_time }}시간
"""

class MarkdownFormatter:
    def format_daily(self, date, logs):
        template = Template(DAILY_TEMPLATE)
        total_time = sum(log.time_spent or 0 for log in logs)
        return template.render(
            date=date.strftime('%Y-%m-%d'),
            logs=logs,
            total_time=total_time
        )
```

---

## 사용 시나리오

### 시나리오 1: 일일 작업 기록

```bash
# 오전
work add "프로젝트 미팅" --category meeting --time 1h

# 오후
work add "API 개발" --category dev --tags python,api --time 3h
work add "코드 리뷰" --category dev --time 0.5h

# 저녁 - 오늘 작업 확인
work list --today

# 노션에 동기화
work sync notion
```

### 시나리오 2: 주간 리포트 생성

```bash
# 금요일 오후
work report --week --output weekly-report.md

# 또는 노션에 직접
work report --week --output notion --title "2025-12-16 주간 리포트"
```

### 시나리오 3: 프로젝트별 시간 추적

```bash
# 통계 확인
work stats --by-project --month

# 결과:
# 프로젝트별 작업 시간 (2025-12월)
# - 백엔드 개발: 45.5h
# - 프론트엔드: 12.0h
# - 문서화: 8.5h
```

---

## Shell 별칭 설정

더 편한 사용을 위한 `.zshrc` 또는 `.bashrc` 설정:

```bash
# 빠른 작업 추가
alias w='work add'
alias wl='work list'
alias wt='work list --today'
alias ws='work sync notion'

# 사용 예
w "버그 수정 완료" --category fix
wt  # 오늘 작업 확인
ws  # 노션 동기화
```

---

## 다음 단계

### 1주차: 기본 구조 (현재)
- [x] 조사 완료
- [ ] 프로젝트 구조 생성
- [ ] CLI 기본 명령어 구현
- [ ] 로컬 저장 (JSON/SQLite)

### 2주차: 노션 연동
- [ ] Notion API 연동
- [ ] 데이터베이스 구조 설계
- [ ] 동기화 로직 구현
- [ ] 에러 처리

### 3주차: 고급 기능
- [ ] 마크다운 문서 생성
- [ ] 통계 및 리포트
- [ ] 시간 추적
- [ ] 템플릿 시스템

### 4주차: 완성 및 문서화
- [ ] 테스트 작성
- [ ] 사용자 문서
- [ ] 배포 준비
- [ ] README 작성

---

## 참고 자료

### Python CLI 프레임워크
- [Click](https://click.palletsprojects.com/)
- [Typer](https://typer.tiangolo.com/)

### Notion API
- [Notion Developers](https://developers.notion.com/)
- [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)

### 유사 프로젝트
- [jrnl](https://jrnl.sh/) - 커맨드라인 저널
- [watson](https://tailordev.github.io/Watson/) - 시간 추적 CLI
- [taskwarrior](https://taskwarrior.org/) - 작업 관리 CLI
