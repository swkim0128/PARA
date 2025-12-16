# 작업 로거 구현 가이드

## 빠른 시작 (Quick Start)

### 1단계: 프로젝트 생성

```bash
# 프로젝트 디렉토리 생성
mkdir work-logger
cd work-logger

# Python 가상환경 생성
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Git 초기화
git init
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".DS_Store" >> .gitignore
```

### 2단계: 기본 파일 생성

#### `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="work-logger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "notion-client>=2.0.0",
        "python-dateutil>=2.8.0",
        "jinja2>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "work=work_logger.cli:cli",
        ],
    },
)
```

#### `requirements.txt`
```txt
click>=8.0.0
notion-client>=2.0.0
python-dateutil>=2.8.0
jinja2>=3.0.0
```

### 3단계: 패키지 구조 생성

```bash
mkdir -p work_logger/{formatters,exporters,utils}
touch work_logger/__init__.py
touch work_logger/cli.py
touch work_logger/models.py
touch work_logger/storage.py
touch work_logger/formatters/__init__.py
touch work_logger/exporters/__init__.py
touch work_logger/utils/__init__.py
```

---

## 핵심 코드 구현

### `work_logger/models.py` - 데이터 모델

```python
"""
작업 로그 데이터 모델
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class WorkLog:
    """작업 로그 엔트리"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    category: str = "general"
    tags: List[str] = field(default_factory=list)
    project: Optional[str] = None
    time_spent: Optional[float] = None  # hours
    created_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'id': self.id,
            'content': self.content,
            'category': self.category,
            'tags': self.tags,
            'project': self.project,
            'time_spent': self.time_spent,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """딕셔너리로부터 생성"""
        data['created_at'] = datetime.fromisoformat(data['created_at'])
        return cls(**data)
```

### `work_logger/storage.py` - 로컬 저장

```python
"""
작업 로그 로컬 저장 (JSON)
"""
import json
from pathlib import Path
from typing import List, Optional
from datetime import date, datetime
from .models import WorkLog

class Storage:
    """JSON 기반 로컬 저장소"""
    
    def __init__(self, data_dir: Path = None):
        if data_dir is None:
            data_dir = Path.home() / '.work-logger'
        self.data_dir = data_dir
        self.data_dir.mkdir(exist_ok=True)
        self.data_file = self.data_dir / 'logs.json'
        self._ensure_file()
    
    def _ensure_file(self):
        """데이터 파일 생성"""
        if not self.data_file.exists():
            self.data_file.write_text('[]')
    
    def add(self, log: WorkLog):
        """작업 로그 추가"""
        logs = self.load_all()
        logs.append(log.to_dict())
        self._save(logs)
    
    def load_all(self) -> List[dict]:
        """모든 로그 로드"""
        return json.loads(self.data_file.read_text())
    
    def load_by_date(self, target_date: date) -> List[WorkLog]:
        """특정 날짜의 로그 로드"""
        all_logs = self.load_all()
        filtered = [
            WorkLog.from_dict(log)
            for log in all_logs
            if datetime.fromisoformat(log['created_at']).date() == target_date
        ]
        return filtered
    
    def load_date_range(self, start: date, end: date) -> List[WorkLog]:
        """날짜 범위의 로그 로드"""
        all_logs = self.load_all()
        filtered = [
            WorkLog.from_dict(log)
            for log in all_logs
            if start <= datetime.fromisoformat(log['created_at']).date() <= end
        ]
        return filtered
    
    def _save(self, logs: List[dict]):
        """저장"""
        self.data_file.write_text(json.dumps(logs, indent=2, ensure_ascii=False))
```

### `work_logger/cli.py` - CLI 인터페이스

```python
"""
CLI 진입점
"""
import click
from datetime import datetime, date, timedelta
from .models import WorkLog
from .storage import Storage

@click.group()
def cli():
    """작업 로거 - 명령어로 작업 기록 및 문서화"""
    pass

@cli.command()
@click.argument('content')
@click.option('--category', '-c', default='general', help='작업 카테고리')
@click.option('--tags', '-t', multiple=True, help='태그 (여러 개 가능)')
@click.option('--project', '-p', help='프로젝트명')
@click.option('--time', type=float, help='소요 시간 (시간 단위)')
def add(content, category, tags, project, time):
    """작업 로그 추가
    
    예시:
        work add "API 개발 완료" -c dev -t python -t api --time 2.5
    """
    log = WorkLog(
        content=content,
        category=category,
        tags=list(tags),
        project=project,
        time_spent=time
    )
    
    storage = Storage()
    storage.add(log)
    
    click.echo(f"✅ 작업이 기록되었습니다: {content}")
    if time:
        click.echo(f"   소요 시간: {time}시간")

@cli.command()
@click.option('--today', is_flag=True, help='오늘 작업만')
@click.option('--week', is_flag=True, help='이번 주 작업')
@click.option('--date', help='특정 날짜 (YYYY-MM-DD)')
@click.option('--project', '-p', help='프로젝트 필터')
def list(today, week, date, project):
    """작업 로그 조회
    
    예시:
        work list --today
        work list --week
        work list --date 2025-12-15
    """
    storage = Storage()
    
    # 날짜 범위 결정
    if today:
        target_date = datetime.now().date()
        logs = storage.load_by_date(target_date)
        title = f"오늘 ({target_date})"
    elif week:
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)
        logs = storage.load_date_range(start_date, end_date)
        title = f"이번 주 ({start_date} ~ {end_date})"
    elif date:
        target_date = datetime.fromisoformat(date).date()
        logs = storage.load_by_date(target_date)
        title = f"{target_date}"
    else:
        # 최근 7일
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)
        logs = storage.load_date_range(start_date, end_date)
        title = f"최근 7일 ({start_date} ~ {end_date})"
    
    # 프로젝트 필터
    if project:
        logs = [log for log in logs if log.project == project]
    
    # 출력
    click.echo(f"\n📋 {title} 작업 로그\n")
    
    if not logs:
        click.echo("   기록된 작업이 없습니다.")
        return
    
    for log in logs:
        time_str = log.created_at.strftime('%H:%M')
        click.echo(f"⏰ {time_str} | {log.content}")
        click.echo(f"   카테고리: {log.category}", nl=False)
        if log.tags:
            click.echo(f" | 태그: {', '.join(log.tags)}", nl=False)
        if log.project:
            click.echo(f" | 프로젝트: {log.project}", nl=False)
        if log.time_spent:
            click.echo(f" | 시간: {log.time_spent}h", nl=False)
        click.echo("\n")
    
    # 총 시간
    total_time = sum(log.time_spent or 0 for log in logs)
    if total_time > 0:
        click.echo(f"📊 총 작업 시간: {total_time:.1f}시간\n")

@cli.command()
@click.option('--week', is_flag=True, help='주간 통계')
@click.option('--month', is_flag=True, help='월간 통계')
@click.option('--by-project', is_flag=True, help='프로젝트별 통계')
@click.option('--by-category', is_flag=True, help='카테고리별 통계')
def stats(week, month, by_project, by_category):
    """작업 통계
    
    예시:
        work stats --week --by-project
        work stats --month --by-category
    """
    storage = Storage()
    
    # 날짜 범위 결정
    if week:
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)
        title = "이번 주"
    elif month:
        today = datetime.now().date()
        start_date = today.replace(day=1)
        end_date = today
        title = "이번 달"
    else:
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=29)
        title = "최근 30일"
    
    logs = storage.load_date_range(start_date, end_date)
    
    click.echo(f"\n📊 {title} 작업 통계 ({start_date} ~ {end_date})\n")
    
    # 기본 통계
    total_logs = len(logs)
    total_time = sum(log.time_spent or 0 for log in logs)
    
    click.echo(f"총 작업 수: {total_logs}개")
    click.echo(f"총 작업 시간: {total_time:.1f}시간\n")
    
    # 프로젝트별 통계
    if by_project:
        from collections import defaultdict
        project_stats = defaultdict(lambda: {'count': 0, 'time': 0})
        
        for log in logs:
            proj = log.project or '(프로젝트 없음)'
            project_stats[proj]['count'] += 1
            project_stats[proj]['time'] += log.time_spent or 0
        
        click.echo("📁 프로젝트별 통계:")
        for proj, stats in sorted(project_stats.items()):
            click.echo(f"  {proj}: {stats['count']}개 작업, {stats['time']:.1f}시간")
        click.echo()
    
    # 카테고리별 통계
    if by_category:
        from collections import defaultdict
        category_stats = defaultdict(lambda: {'count': 0, 'time': 0})
        
        for log in logs:
            category_stats[log.category]['count'] += 1
            category_stats[log.category]['time'] += log.time_spent or 0
        
        click.echo("🏷️  카테고리별 통계:")
        for cat, stats in sorted(category_stats.items()):
            click.echo(f"  {cat}: {stats['count']}개 작업, {stats['time']:.1f}시간")

if __name__ == '__main__':
    cli()
```

---

## 설치 및 사용

### 1. 개발 모드로 설치

```bash
# 프로젝트 디렉토리에서
pip install -e .

# 또는 의존성만 설치
pip install -r requirements.txt
```

### 2. 기본 사용법

```bash
# 작업 추가
work add "프로젝트 설정 완료"
work add "API 개발" -c dev -t python --time 2.5

# 오늘 작업 확인
work list --today

# 이번 주 작업 확인
work list --week

# 통계
work stats --week --by-project
```

### 3. Shell 별칭 설정

`~/.zshrc` 또는 `~/.bashrc`에 추가:

```bash
# 작업 로거 별칭
alias w='work add'
alias wl='work list'
alias wt='work list --today'
alias ww='work list --week'
alias wst='work stats'

# 사용 예
w "버그 수정" -c fix
wt
wst --week --by-project
```

---

## 노션 연동 (선택)

### 1. Notion API 토큰 발급

1. [Notion Developers](https://www.notion.so/my-integrations) 접속
2. **New integration** 클릭
3. 이름 입력 후 **Submit**
4. **Internal Integration Token** 복사

### 2. Notion 데이터베이스 생성

1. Notion에서 새 페이지 생성
2. **Table - Full page** 선택
3. 컬럼 구성:
   - 제목 (Title)
   - 카테고리 (Select)
   - 태그 (Multi-select)
   - 프로젝트 (Text)
   - 작업 시간 (Number)
   - 날짜 (Date)
4. Share → Add connections → 생성한 Integration 선택
5. 데이터베이스 URL에서 ID 복사
   ```
   https://notion.so/workspace/{database_id}?v=...
   ```

### 3. 환경 변수 설정

```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export NOTION_TOKEN="secret_xxxxxxxxxxxx"
export NOTION_DATABASE_ID="xxxxx-xxxxx-xxxxx"
```

### 4. Notion 내보내기 구현

`work_logger/exporters/notion_export.py`:

```python
"""
Notion 내보내기
"""
from notion_client import Client
from ..models import WorkLog

class NotionExporter:
    def __init__(self, token, database_id):
        self.client = Client(auth=token)
        self.database_id = database_id
    
    def export_log(self, log: WorkLog):
        """작업 로그를 Notion 페이지로 생성"""
        properties = {
            "제목": {
                "title": [{"text": {"content": log.content}}]
            },
            "카테고리": {
                "select": {"name": log.category}
            },
            "날짜": {
                "date": {"start": log.created_at.isoformat()}
            }
        }
        
        if log.tags:
            properties["태그"] = {
                "multi_select": [{"name": tag} for tag in log.tags]
            }
        
        if log.project:
            properties["프로젝트"] = {
                "rich_text": [{"text": {"content": log.project}}]
            }
        
        if log.time_spent:
            properties["작업 시간"] = {
                "number": log.time_spent
            }
        
        return self.client.pages.create(
            parent={"database_id": self.database_id},
            properties=properties
        )
```

CLI 명령어 추가 (`cli.py`):

```python
@cli.command()
@click.option('--today', is_flag=True, help='오늘 작업만 동기화')
def sync(today):
    """Notion으로 동기화
    
    예시:
        work sync
        work sync --today
    """
    import os
    from .exporters.notion_export import NotionExporter
    
    token = os.environ.get('NOTION_TOKEN')
    db_id = os.environ.get('NOTION_DATABASE_ID')
    
    if not token or not db_id:
        click.echo("❌ NOTION_TOKEN 또는 NOTION_DATABASE_ID가 설정되지 않았습니다.", err=True)
        return
    
    storage = Storage()
    exporter = NotionExporter(token, db_id)
    
    if today:
        logs = storage.load_by_date(datetime.now().date())
    else:
        # 최근 7일
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)
        logs = storage.load_date_range(start_date, end_date)
    
    click.echo(f"📤 {len(logs)}개 작업을 Notion에 동기화 중...")
    
    for log in logs:
        try:
            exporter.export_log(log)
            click.echo(f"  ✅ {log.content}")
        except Exception as e:
            click.echo(f"  ❌ {log.content}: {e}", err=True)
    
    click.echo("\n✨ 동기화 완료!")
```

---

## 마크다운 문서 생성

### `work_logger/formatters/markdown.py`

```python
"""
마크다운 포맷터
"""
from typing import List
from datetime import date
from jinja2 import Template
from ..models import WorkLog

DAILY_TEMPLATE = """# {{ date }}

## 📋 작업 내역

{% for log in logs %}
### {{ log.created_at.strftime('%H:%M') }} - {{ log.content }}

- **카테고리**: {{ log.category }}
{% if log.tags %}
- **태그**: {{ log.tags | join(', ') }}
{% endif %}
{% if log.project %}
- **프로젝트**: {{ log.project }}
{% endif %}
{% if log.time_spent %}
- **소요 시간**: {{ log.time_spent }}시간
{% endif %}

{% endfor %}

## 📊 요약

- **총 작업 수**: {{ logs | length }}개
- **총 작업 시간**: {{ total_time }}시간
"""

class MarkdownFormatter:
    def format_daily(self, target_date: date, logs: List[WorkLog]) -> str:
        """일일 리포트 생성"""
        template = Template(DAILY_TEMPLATE)
        total_time = sum(log.time_spent or 0 for log in logs)
        return template.render(
            date=target_date.strftime('%Y년 %m월 %d일'),
            logs=logs,
            total_time=total_time
        )
```

CLI 명령어 추가:

```python
@cli.command()
@click.option('--today', is_flag=True, help='오늘 리포트')
@click.option('--output', '-o', help='출력 파일 경로')
def report(today, output):
    """마크다운 리포트 생성
    
    예시:
        work report --today
        work report --today -o daily-report.md
    """
    from .formatters.markdown import MarkdownFormatter
    
    storage = Storage()
    formatter = MarkdownFormatter()
    
    if today:
        target_date = datetime.now().date()
        logs = storage.load_by_date(target_date)
    else:
        target_date = datetime.now().date()
        logs = storage.load_by_date(target_date)
    
    markdown = formatter.format_daily(target_date, logs)
    
    if output:
        Path(output).write_text(markdown, encoding='utf-8')
        click.echo(f"✅ 리포트가 생성되었습니다: {output}")
    else:
        click.echo(markdown)
```

---

## 다음 단계

### 완성도 높이기
- [ ] 설정 관리 (config.yaml)
- [ ] 작업 수정/삭제 기능
- [ ] 템플릿 시스템
- [ ] 주간/월간 리포트
- [ ] 데이터 백업/복원

### 테스트
- [ ] 단위 테스트 작성
- [ ] 통합 테스트
- [ ] CLI 테스트

### 배포
- [ ] PyPI에 패키지 업로드
- [ ] Homebrew formula 작성
- [ ] 사용자 문서 작성
