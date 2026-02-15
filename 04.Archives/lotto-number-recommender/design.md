# 로또 번호 추천기 설계 문서

## 1. 시스템 아키텍처

### 전체 구조
```
┌─────────────────────────────────────────────────┐
│                  사용자                          │
└───────────────┬─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────┐
│              CLI 인터페이스                      │
│  - 번호 추천 요청                                │
│  - 통계 조회                                     │
│  - 수동 데이터 업데이트                          │
└───────────────┬─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────┐
│           추천 엔진 (Recommender)                │
│  - 분석 결과 통합                                │
│  - 가중치 계산                                   │
│  - 최종 번호 선정                                │
└───────────┬──────────────┬──────────────────────┘
            │              │
            ▼              ▼
┌──────────────────┐  ┌──────────────────────────┐
│  데이터 분석기    │  │    데이터 수집기          │
│  (Analyzer)      │  │    (Crawler)             │
│  - 빈도 분석     │  │  - API 호출               │
│  - 패턴 분석     │  │  - 데이터 파싱            │
│  - 추세 분석     │  │  - DB 저장                │
└────────┬─────────┘  └──────────┬───────────────┘
         │                       │
         ▼                       ▼
┌─────────────────────────────────────────────────┐
│              데이터베이스 (SQLite)                │
│  - lotto_results: 당첨 번호 저장                 │
│  - analysis_cache: 분석 결과 캐싱                │
└─────────────────────────────────────────────────┘
         ▲
         │
┌────────┴─────────┐
│   스케줄러        │
│  (Scheduler)     │
│  - 매주 토요일    │
│    자동 크롤링    │
└──────────────────┘
```

## 2. 데이터베이스 설계

### 2.1 lotto_results 테이블
```sql
CREATE TABLE lotto_results (
    round INTEGER PRIMARY KEY,           -- 회차 (1부터 시작)
    draw_date DATE NOT NULL,             -- 추첨 날짜
    num1 INTEGER NOT NULL CHECK(num1 BETWEEN 1 AND 45),
    num2 INTEGER NOT NULL CHECK(num2 BETWEEN 1 AND 45),
    num3 INTEGER NOT NULL CHECK(num3 BETWEEN 1 AND 45),
    num4 INTEGER NOT NULL CHECK(num4 BETWEEN 1 AND 45),
    num5 INTEGER NOT NULL CHECK(num5 BETWEEN 1 AND 45),
    num6 INTEGER NOT NULL CHECK(num6 BETWEEN 1 AND 45),
    bonus_num INTEGER NOT NULL CHECK(bonus_num BETWEEN 1 AND 45),
    first_prize BIGINT,                  -- 1등 당첨금
    first_winner_count INTEGER,          -- 1등 당첨자 수
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(num1, num2, num3, num4, num5, num6)
);

-- 인덱스
CREATE INDEX idx_draw_date ON lotto_results(draw_date);
CREATE INDEX idx_round ON lotto_results(round DESC);
```

### 2.2 number_frequency 테이블 (분석 캐시)
```sql
CREATE TABLE number_frequency (
    number INTEGER PRIMARY KEY CHECK(number BETWEEN 1 AND 45),
    total_count INTEGER DEFAULT 0,       -- 전체 출현 횟수
    recent_10_count INTEGER DEFAULT 0,   -- 최근 10회 출현
    recent_20_count INTEGER DEFAULT 0,   -- 최근 20회 출현
    recent_50_count INTEGER DEFAULT 0,   -- 최근 50회 출현
    last_appeared_round INTEGER,         -- 마지막 출현 회차
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2.3 recommendations 테이블 (추천 이력)
```sql
CREATE TABLE recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recommended_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    num1 INTEGER, num2 INTEGER, num3 INTEGER,
    num4 INTEGER, num5 INTEGER, num6 INTEGER,
    algorithm_version VARCHAR(20),       -- 알고리즘 버전
    confidence_score FLOAT,              -- 신뢰도 점수
    notes TEXT
);
```

## 3. 주요 모듈 설계

### 3.1 Crawler 모듈 (crawler.py)

#### 클래스: LottoCrawler
```python
class LottoCrawler:
    def __init__(self, db_path: str):
        """
        로또 데이터 크롤러 초기화
        
        Args:
            db_path: 데이터베이스 파일 경로
        """
        self.db = Database(db_path)
        self.api_url = "https://www.dhlottery.co.kr/common.do"
    
    def get_latest_round(self) -> int:
        """현재 최신 회차 번호 가져오기"""
        pass
    
    def fetch_lotto_data(self, round_num: int) -> dict:
        """
        특정 회차의 로또 데이터 가져오기
        
        Args:
            round_num: 회차 번호
            
        Returns:
            dict: 로또 데이터
        """
        pass
    
    def save_to_db(self, data: dict) -> bool:
        """데이터베이스에 저장"""
        pass
    
    def crawl_all(self, start_round: int = 1) -> None:
        """초기 데이터 수집 (1회차부터 최신까지)"""
        pass
    
    def update_latest(self) -> None:
        """최신 회차 데이터만 업데이트"""
        pass
```

### 3.2 Analyzer 모듈 (analyzer.py)

#### 클래스: LottoAnalyzer
```python
class LottoAnalyzer:
    def __init__(self, db_path: str):
        self.db = Database(db_path)
    
    def calculate_frequency(self, recent_n: int = None) -> dict:
        """
        번호별 출현 빈도 계산
        
        Args:
            recent_n: 최근 N회차만 분석 (None이면 전체)
            
        Returns:
            dict: {번호: 출현횟수}
        """
        pass
    
    def analyze_patterns(self) -> dict:
        """
        패턴 분석
        - 연속 번호 출현 비율
        - 홀짝 비율
        - 구간별 분포
        
        Returns:
            dict: 패턴 분석 결과
        """
        pass
    
    def analyze_recent_trend(self, window: int = 10) -> dict:
        """최근 추세 분석"""
        pass
    
    def get_cold_numbers(self, threshold: int = 10) -> list:
        """오랫동안 미출현 번호 찾기"""
        pass
    
    def get_hot_numbers(self, recent_n: int = 10) -> list:
        """최근 자주 출현한 번호 찾기"""
        pass
```

### 3.3 Recommender 모듈 (recommender.py)

#### 클래스: LottoRecommender
```python
class LottoRecommender:
    def __init__(self, db_path: str):
        self.analyzer = LottoAnalyzer(db_path)
        self.db = Database(db_path)
        
        # 가중치 설정
        self.weights = {
            'frequency': 0.4,      # 출현 빈도
            'pattern': 0.3,        # 패턴 적합도
            'trend': 0.3           # 최근 추세
        }
    
    def calculate_scores(self) -> dict:
        """
        각 번호의 종합 점수 계산
        
        Returns:
            dict: {번호: 점수}
        """
        # 1. 빈도 점수
        frequency_scores = self._calc_frequency_score()
        
        # 2. 패턴 점수
        pattern_scores = self._calc_pattern_score()
        
        # 3. 추세 점수
        trend_scores = self._calc_trend_score()
        
        # 종합 점수
        total_scores = {}
        for num in range(1, 46):
            total_scores[num] = (
                frequency_scores[num] * self.weights['frequency'] +
                pattern_scores[num] * self.weights['pattern'] +
                trend_scores[num] * self.weights['trend']
            )
        
        return total_scores
    
    def recommend(self, count: int = 6, 
                  exclude: list = None,
                  include: list = None) -> list:
        """
        번호 추천
        
        Args:
            count: 추천할 번호 개수
            exclude: 제외할 번호 리스트
            include: 반드시 포함할 번호 리스트
            
        Returns:
            list: 추천 번호 리스트 (오름차순)
        """
        pass
    
    def recommend_multiple(self, sets: int = 5) -> list:
        """여러 조합 추천"""
        pass
    
    def save_recommendation(self, numbers: list) -> None:
        """추천 결과 저장"""
        pass
```

### 3.4 Scheduler 모듈 (scheduler.py)

```python
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

class LottoScheduler:
    def __init__(self, crawler: LottoCrawler):
        self.crawler = crawler
        self.scheduler = BlockingScheduler()
    
    def setup_jobs(self):
        """작업 스케줄 설정"""
        # 매주 토요일 오후 9시에 업데이트
        self.scheduler.add_job(
            self.update_job,
            'cron',
            day_of_week='sat',
            hour=21,
            minute=0
        )
    
    def update_job(self):
        """정기 업데이트 작업"""
        print(f"[{datetime.now()}] 로또 데이터 업데이트 시작")
        try:
            self.crawler.update_latest()
            print("업데이트 완료")
        except Exception as e:
            print(f"업데이트 실패: {e}")
    
    def start(self):
        """스케줄러 시작"""
        print("로또 자동 업데이트 스케줄러 시작")
        self.scheduler.start()
```

## 4. 분석 알고리즘 상세

### 4.1 빈도 점수 계산
```python
def _calc_frequency_score(self) -> dict:
    """
    출현 빈도 기반 점수
    - 전체 빈도: 40%
    - 최근 50회: 30%
    - 최근 20회: 20%
    - 최근 10회: 10%
    """
    scores = {}
    
    # 데이터 가져오기
    total_freq = self.analyzer.calculate_frequency()
    freq_50 = self.analyzer.calculate_frequency(recent_n=50)
    freq_20 = self.analyzer.calculate_frequency(recent_n=20)
    freq_10 = self.analyzer.calculate_frequency(recent_n=10)
    
    # 정규화 및 가중치 적용
    for num in range(1, 46):
        scores[num] = (
            normalize(total_freq[num]) * 0.4 +
            normalize(freq_50[num]) * 0.3 +
            normalize(freq_20[num]) * 0.2 +
            normalize(freq_10[num]) * 0.1
        )
    
    return scores
```

### 4.2 패턴 점수 계산
```python
def _calc_pattern_score(self) -> dict:
    """
    패턴 적합도 점수
    - 홀짝 균형
    - 구간 분포 균형
    - 연속 번호 회피
    """
    scores = {num: 0.5 for num in range(1, 46)}  # 기본 점수
    
    patterns = self.analyzer.analyze_patterns()
    
    # 홀짝 비율이 3:3에 가까운 번호에 가점
    # 최근 당첨 번호의 구간 분포와 다른 구간에 가점
    # 최근 연속 번호가 많았다면 연속되지 않은 번호에 가점
    
    return scores
```

### 4.3 추세 점수 계산
```python
def _calc_trend_score(self) -> dict:
    """
    최근 출현 추세 점수
    - 최근 N회차 동안의 출현 변화율
    - 미출현 기간에 따른 가중치
    """
    scores = {}
    trend = self.analyzer.analyze_recent_trend(window=10)
    
    for num in range(1, 46):
        # 최근 출현 증가 추세면 높은 점수
        # 오래 미출현이면 중간 점수
        # 최근 과다 출현이면 낮은 점수
        scores[num] = calculate_trend_score(trend[num])
    
    return scores
```

## 5. CLI 인터페이스

### 명령어 구조
```bash
# 번호 추천
python cli.py recommend [옵션]
  --count N          # 추천할 번호 개수 (기본: 6)
  --exclude 1,2,3    # 제외할 번호
  --include 7,14     # 반드시 포함할 번호
  --sets N           # 여러 조합 생성 (기본: 1)

# 통계 조회
python cli.py stats
  --frequency        # 빈도 통계
  --patterns         # 패턴 분석
  --hot              # 핫 번호
  --cold             # 콜드 번호

# 데이터 업데이트
python cli.py update
  --initial          # 전체 데이터 초기 수집
  --latest           # 최신 회차만 업데이트

# 스케줄러 시작
python cli.py schedule
```

## 6. 개발 단계

### Phase 1: 기본 인프라 (1주)
- [x] 프로젝트 구조 설정
- [ ] 데이터베이스 스키마 구현
- [ ] 크롤러 기본 기능 구현
- [ ] 초기 데이터 수집

### Phase 2: 분석 엔진 (2주)
- [ ] 빈도 분석 알고리즘
- [ ] 패턴 분석 알고리즘
- [ ] 추세 분석 알고리즘
- [ ] 캐싱 시스템 구현

### Phase 3: 추천 시스템 (1주)
- [ ] 점수 계산 로직
- [ ] 추천 알고리즘 구현
- [ ] 옵션 처리 (exclude, include)

### Phase 4: 자동화 (1주)
- [ ] 스케줄러 구현
- [ ] 에러 처리 및 로깅
- [ ] 모니터링 시스템

### Phase 5: UI 및 개선 (1주)
- [ ] CLI 인터페이스 완성
- [ ] 결과 시각화
- [ ] 성능 최적화
- [ ] 문서화

## 7. 테스트 계획

### 7.1 단위 테스트
- 크롤러: API 호출, 데이터 파싱
- 분석기: 각 분석 알고리즘
- 추천기: 점수 계산, 번호 선정

### 7.2 통합 테스트
- 전체 워크플로우
- 스케줄러 동작
- 데이터 무결성

### 7.3 성능 테스트
- 대용량 데이터 처리 (1000회차+)
- 분석 속도
- 메모리 사용량

## 8. 향후 개선 사항

### 8.1 머신러닝 도입
- 딥러닝 모델로 패턴 학습
- LSTM으로 시계열 분석
- 앙상블 모델 적용

### 8.2 웹 인터페이스
- Flask/FastAPI로 REST API 구축
- React로 프론트엔드 구현
- 실시간 통계 대시보드

### 8.3 고급 분석
- 요일별 패턴 분석
- 계절별 패턴 분석
- 특이값 탐지

## 9. 참고 자료

- [동행복권 API 문서](https://dhlottery.co.kr/)
- [APScheduler 공식 문서](https://apscheduler.readthedocs.io/)
- [pandas 공식 문서](https://pandas.pydata.org/)
- 통계학 기초 이론
