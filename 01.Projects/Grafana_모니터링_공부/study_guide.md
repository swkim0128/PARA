# Grafana 모니터링 학습 가이드

## 🔗 Notion 연동

> ⚠️ **2026-08-17 방향 전환** — 옛 "Notion → PARA 단방향, 직접 편집 금지" 규약은 폐기됐다. 이제 **볼트가 실질 SoT**이고 노션은 상태 인덱스이며, 이 문서는 직접 편집한다. 규칙 정본 → `02.Areas/07.개인관리/05.프로젝트.md`
> 자동 동기화는 2026-05-19 이후 정지 상태 — 아래 값은 수동 갱신한다.

- **Notion ID**: [PRO-110](https://www.notion.so/2cba25196d34812eac25ffcc700233c3)
- **Status**: Paused _(2026-08-17 정정 — 산출물이 2026-02-22 이후 정지)_
- **Priority**: 높음
- **Tags**: 개인, 공부
- **Start Date**: 2025-12-17
- **End Date**: _(미정)_
- **Description**: 업무 환경에서 Grafana를 활용한 애플리케이션 모니터링 시스템 구축 학습

## 📚 학습 목차

## 1. Grafana 기초
## 2. 데이터 소스 연결
## 3. 대시보드 구축
## 4. 쿼리 작성
## 5. 알람 시스템
## 6. 고급 기능

---

## 1. Grafana 기초

## 1.1 Grafana란?
Grafana는 오픈소스 메트릭 분석 및 시각화 플랫폼입니다.
- 다양한 데이터 소스 지원
- 실시간 모니터링
- 대시보드를 통한 시각화
- 알람 및 알림 기능

## 1.2 설치 방법

## Docker로 설치 (권장)
```bash
# Grafana 컨테이너 실행
docker run -d \
  -p 3000:3000 \
  --name=grafana \
  -v grafana-storage:/var/lib/grafana \
  grafana/grafana-enterprise

# 접속
http://localhost:3000
# 기본 계정: admin / admin
```

## macOS 직접 설치
```bash
# Homebrew로 설치
brew install grafana

# 서비스 시작
brew services start grafana

# 접속
http://localhost:3000
```

## Linux 직접 설치
```bash
# Ubuntu/Debian
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install grafana

# 서비스 시작
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

## 1.3 기본 UI 구조

**주요 메뉴**:
- **Home**: 홈 대시보드
- **Dashboards**: 대시보드 목록
- **Explore**: 데이터 탐색 (임시 쿼리)
- **Alerting**: 알람 규칙 관리
- **Configuration**: 설정
  - Data Sources: 데이터 소스 관리
  - Users: 사용자 관리
  - Teams: 팀 관리
  - Plugins: 플러그인 관리

## 1.4 사용자 및 권한 관리

**권한 레벨**:
- **Admin**: 모든 권한
- **Editor**: 대시보드 생성/수정
- **Viewer**: 읽기 전용

**조직(Organization)**:
- 여러 조직 생성 가능
- 조직별 독립적인 대시보드/데이터 소스

---

## 2. 데이터 소스 연결

## 2.1 Prometheus 연결

Prometheus는 Grafana에서 가장 많이 사용되는 데이터 소스입니다.

## Prometheus 설치 (Docker)
```bash
# Prometheus 실행
docker run -d \
  -p 9090:9090 \
  --name prometheus \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

## prometheus.yml 설정 예시
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

## Grafana에서 Prometheus 연결
1. **Configuration** > **Data Sources** 클릭
2. **Add data source** 클릭
3. **Prometheus** 선택
4. 설정:
   - Name: `Prometheus`
   - URL: `http://localhost:9090` (Docker인 경우 `http://host.docker.internal:9090`)
5. **Save & Test** 클릭

## 2.2 InfluxDB 연결

## InfluxDB 설치 (Docker)
```bash
docker run -d \
  -p 8086:8086 \
  --name influxdb \
  -v influxdb-data:/var/lib/influxdb2 \
  influxdb:2.0
```

## Grafana에서 InfluxDB 연결
1. **Add data source** > **InfluxDB** 선택
2. 설정:
   - Query Language: **Flux** 또는 **InfluxQL**
   - URL: `http://localhost:8086`
   - Organization: 조직명
   - Token: API 토큰
   - Default Bucket: 버킷명
3. **Save & Test**

## 2.3 MySQL/PostgreSQL 연결

## Grafana에서 MySQL 연결
1. **Add data source** > **MySQL** 선택
2. 설정:
   - Host: `localhost:3306`
   - Database: 데이터베이스명
   - User: 사용자명
   - Password: 비밀번호
   - Max open connections: 100
   - Max idle connections: 2
3. **Save & Test**

## 2.4 Elasticsearch 연결

1. **Add data source** > **Elasticsearch** 선택
2. 설정:
   - URL: `http://localhost:9200`
   - Index name: 인덱스 패턴 (예: `logs-*`)
   - Time field name: `@timestamp`
   - Version: Elasticsearch 버전
3. **Save & Test**

---

## 3. 대시보드 구축

## 3.1 새 대시보드 생성

1. **Dashboards** > **New Dashboard** 클릭
2. **Add visualization** 클릭
3. 데이터 소스 선택
4. 쿼리 작성 및 시각화 설정

## 3.2 패널 종류

## Time Series (시계열 그래프)
- 시간에 따른 데이터 변화 표시
- CPU, 메모리, 네트워크 트래픽 등

## Stat (통계)
- 단일 값 또는 최근 값 표시
- 큰 숫자로 강조
- 임계값에 따른 색상 변경

## Gauge (게이지)
- 현재 값을 게이지 형태로 표시
- 백분율, 사용률 등

## Bar Gauge (막대 게이지)
- 여러 값을 막대로 비교
- 수평/수직 방향 선택 가능

## Table (테이블)
- 데이터를 표 형식으로 표시
- 로그, 이벤트 목록 등

## Heatmap (히트맵)
- 데이터 분포를 색상으로 표시
- 시간대별 분포 분석

## Pie Chart (파이 차트)
- 비율을 원형으로 표시
- 비중 비교

## 3.3 패널 옵션 설정

## Panel Title & Description
- Title: 패널 제목
- Description: 설명 (마우스 오버 시 표시)

## Legend (범례)
- Display mode: List, Table, Hidden
- Placement: Bottom, Right
- Values: 표시할 통계값 (Min, Max, Mean 등)

## Graph Styles
- Line width: 선 두께
- Fill opacity: 영역 투명도
- Point size: 포인트 크기
- Line interpolation: 선 보간 방식

## Axis
- Scale: Linear, Logarithmic
- Unit: 단위 (bytes, percent, seconds 등)
- Min/Max: 축 범위

## Thresholds (임계값)
- 값에 따른 색상 변경
- 예: 80% 이상 빨강, 50-80% 노랑, 50% 이하 초록

## 3.4 레이아웃 구성

## Row 사용
- 패널을 그룹으로 묶기
- Row 접기/펼치기
- Row별 변수 설정

## 패널 배치
- 드래그 앤 드롭으로 위치 조정
- 패널 크기 조절
- 그리드 스냅

## 3.5 시간 범위 설정

## 상대 시간
- Last 5 minutes
- Last 15 minutes
- Last 1 hour
- Last 24 hours
- Last 7 days

## 절대 시간
- 시작 날짜/시간 지정
- 종료 날짜/시간 지정

## 자동 새로고침
- 5s, 10s, 30s, 1m, 5m
- Dashboard settings에서 설정

---

## 4. 쿼리 작성

## 4.1 PromQL (Prometheus Query Language)

## 기본 쿼리
```promql
# 단일 메트릭
node_cpu_seconds_total

# 레이블 필터
node_cpu_seconds_total{mode="idle"}

# 여러 조건
node_cpu_seconds_total{mode="idle",cpu="0"}
```

## 레이트 함수
```promql
# 초당 증가율
rate(node_cpu_seconds_total[5m])

# 분당 증가율
rate(node_cpu_seconds_total[5m]) * 60

# CPU 사용률 (%)
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

## 집계 함수
```promql
# 평균
avg(node_memory_MemAvailable_bytes)

# 합계
sum(rate(http_requests_total[5m]))

# 최대값
max(node_cpu_seconds_total)

# 그룹별 집계
sum by (job) (rate(http_requests_total[5m]))
```

## 연산자
```promql
# 산술 연산
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# 비교 연산
node_filesystem_avail_bytes < 10000000000
```

## 4.2 InfluxQL

## 기본 쿼리
```sql
SELECT "value" FROM "cpu_usage" WHERE time > now() - 1h

SELECT mean("value") FROM "cpu_usage" WHERE time > now() - 1h GROUP BY time(1m)
```

## 4.3 Flux (InfluxDB 2.x)

```flux
from(bucket: "telegraf")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> filter(fn: (r) => r._field == "usage_idle")
  |> aggregateWindow(every: 1m, fn: mean)
```

## 4.4 SQL 쿼리 (MySQL/PostgreSQL)

```sql
SELECT 
  created_at as time,
  COUNT(*) as count
FROM orders
WHERE created_at > NOW() - INTERVAL 1 HOUR
GROUP BY time
ORDER BY time
```

## 4.5 변수 활용

## 변수 생성
1. **Dashboard settings** > **Variables** > **Add variable**
2. 설정:
   - Name: `server`
   - Type: **Query**
   - Data source: Prometheus
   - Query: `label_values(node_cpu_seconds_total, instance)`

## 변수 사용
```promql
# 쿼리에서 변수 사용
node_cpu_seconds_total{instance="$server"}

# 여러 값 선택
node_cpu_seconds_total{instance=~"$server"}
```

---

## 5. 알람 시스템

## 5.1 Alert Rules 설정

## Contact Point 설정 (Notification Channel)
1. **Alerting** > **Contact points** > **New contact point**
2. 이름 입력
3. Integration 선택:
   - **Email**: SMTP 설정
   - **Slack**: Webhook URL
   - **PagerDuty**: Integration Key
   - **Webhook**: Custom URL

## Email 설정 예시
```ini
# grafana.ini 파일
[smtp]
enabled = true
host = smtp.gmail.com:587
user = your-email@gmail.com
password = your-app-password
from_address = your-email@gmail.com
from_name = Grafana
```

## Slack Webhook 설정
1. Slack에서 Incoming Webhook 생성
2. Webhook URL 복사
3. Grafana Contact Point에서 Slack Webhook URL 입력

## 5.2 Alert Rule 생성

1. **Alerting** > **Alert rules** > **New alert rule**
2. 설정:
   - **Rule name**: 알람 이름
   - **Query**: 모니터링할 쿼리
   - **Condition**: 알람 조건
   - **Evaluate every**: 평가 주기
   - **For**: 조건 유지 시간

## 알람 조건 예시

**CPU 사용률 80% 이상**
```promql
Query: 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
Condition: IS ABOVE 80
```

**메모리 사용률 90% 이상**
```promql
Query: (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100
Condition: IS ABOVE 90
```

**디스크 사용량 90% 이상**
```promql
Query: (node_filesystem_size_bytes - node_filesystem_avail_bytes) / node_filesystem_size_bytes * 100
Condition: IS ABOVE 90
```

## 5.3 알람 상태

- **Normal**: 정상
- **Pending**: 조건 충족 중 (For 시간 대기)
- **Alerting**: 알람 발생
- **No Data**: 데이터 없음
- **Error**: 에러 발생

## 5.4 알람 그룹 및 라벨

**라벨 사용**:
- severity: critical, warning, info
- team: backend, frontend, devops
- environment: production, staging, development

**알람 그룹**:
- 같은 라벨을 가진 알람을 그룹화
- 알람 폭주 방지

---

## 6. 고급 기능

## 6.1 템플릿 변수

## 종류
- **Query**: 데이터 소스에서 값 가져오기
- **Custom**: 수동으로 값 입력
- **Constant**: 고정 값
- **Text box**: 사용자 입력
- **Interval**: 시간 간격

## 체인 변수
```promql
# 첫 번째 변수: region
label_values(node_cpu_seconds_total, datacenter)

# 두 번째 변수: server (region에 의존)
label_values(node_cpu_seconds_total{datacenter="$region"}, instance)
```

## 6.2 애노테이션 (Annotations)

## 애노테이션 추가
1. **Dashboard settings** > **Annotations**
2. **New annotation** 클릭
3. 데이터 소스 및 쿼리 설정

## 사용 예시
- 배포 이벤트 표시
- 장애 발생 시점 표시
- 설정 변경 이력

## 6.3 플러그인

## 설치 방법
```bash
# Grafana CLI로 설치
grafana-cli plugins install <plugin-id>

# 예: Worldmap Panel 설치
grafana-cli plugins install grafana-worldmap-panel

# Grafana 재시작
sudo systemctl restart grafana-server
```

## 유용한 플러그인
- **Worldmap Panel**: 지도 시각화
- **Clock Panel**: 시계 표시
- **Pie Chart Panel**: 파이 차트
- **Stat Panel**: 통계 표시

## 6.4 Provisioning (자동 구성)

## 데이터 소스 Provisioning
```yaml
# /etc/grafana/provisioning/datasources/datasource.yml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://localhost:9090
    isDefault: true
```

## 대시보드 Provisioning
```yaml
# /etc/grafana/provisioning/dashboards/dashboard.yml
apiVersion: 1

providers:
  - name: 'default'
    orgId: 1
    folder: ''
    type: file
    options:
      path: /var/lib/grafana/dashboards
```

## 6.5 API 활용

## 대시보드 내보내기
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  http://localhost:3000/api/dashboards/uid/YOUR_DASHBOARD_UID
```

## 알람 상태 조회
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  http://localhost:3000/api/alerts
```

---

## 📊 실습 프로젝트

## 프로젝트 1: 시스템 모니터링 대시보드

**목표**: Node Exporter로 시스템 메트릭 수집 및 시각화

**단계**:
1. Node Exporter 설치
```bash
docker run -d \
  -p 9100:9100 \
  --name node-exporter \
  prom/node-exporter
```

2. Prometheus 설정에 Node Exporter 추가
```yaml
scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['host.docker.internal:9100']
```

3. Grafana에서 대시보드 생성
   - CPU 사용률
   - 메모리 사용률
   - 디스크 사용량
   - 네트워크 트래픽

## 프로젝트 2: 애플리케이션 모니터링

**목표**: 애플리케이션 메트릭 수집 및 분석

**메트릭**:
- API 요청 수
- 응답 시간
- 에러율
- 데이터베이스 커넥션 풀

**알람 설정**:
- 응답 시간 > 1초
- 에러율 > 5%
- DB 커넥션 > 80%

## 프로젝트 3: 비즈니스 메트릭 대시보드

**목표**: 비즈니스 KPI 시각화

**메트릭**:
- 일일 활성 사용자
- 신규 가입자
- 매출
- 전환율

---

## 🔍 트러블슈팅

## 문제 1: 데이터가 표시되지 않음
**원인**: 시간 범위가 데이터 없는 구간
**해결**: 시간 범위 조정

## 문제 2: 쿼리 에러
**원인**: 잘못된 PromQL 문법
**해결**: Prometheus UI에서 쿼리 테스트

## 문제 3: 알람이 작동하지 않음
**원인**: Contact Point 설정 오류
**해결**: Test 버튼으로 알림 테스트

## 문제 4: 대시보드 로딩이 느림
**원인**: 쿼리가 너무 복잡하거나 데이터가 많음
**해결**: 
- 시간 범위 줄이기
- 집계 간격 늘리기
- 인덱스 생성

---

## 📚 추가 학습 자료

## 공식 문서
- [Grafana Documentation](https://grafana.com/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)

## 튜토리얼
- [Grafana Fundamentals](https://grafana.com/tutorials/grafana-fundamentals/)
- [PromQL for Humans](https://timber.io/blog/promql-for-humans/)

## 영상
- [Grafana Labs YouTube](https://www.youtube.com/c/Grafana)
- [Introduction to Grafana](https://www.youtube.com/watch?v=Bb1n77xvmqc)

## 커뮤니티
- [Grafana Community Forums](https://community.grafana.com/)
- [r/grafana Reddit](https://www.reddit.com/r/grafana/)

---

## ✅ 학습 체크리스트

## 기초
- [ ] Grafana 설치 및 실행
- [ ] 기본 UI 이해
- [ ] 첫 번째 대시보드 생성

## 중급
- [ ] Prometheus 연동
- [ ] PromQL 기본 쿼리 작성
- [ ] 다양한 패널 타입 활용
- [ ] 변수 사용
- [ ] 알람 설정

## 고급
- [ ] 복잡한 PromQL 쿼리
- [ ] 커스텀 플러그인 사용
- [ ] API를 통한 자동화
- [ ] Provisioning 설정
- [ ] 성능 최적화
