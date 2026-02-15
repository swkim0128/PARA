# 네이버 카페 게시판 이미지 크롤러

네이버 카페 게시판에서 오래된 순서대로 게시글을 탐색하고 이미지를 자동으로 다운로드하는 도구입니다.

## 프로젝트 개요

**목적**: 네이버 카페 게시판의 이미지를 효율적으로 백업/아카이빙  
**상태**: 개발 완료  
**작성일**: 2024-12-20

## 주요 기능

- ✅ 게시판 마지막 페이지(가장 오래된 게시글)부터 자동 탐색
- ✅ 모든 게시글 순회하며 이미지 자동 검색
- ✅ 이미지 다운로드 (제목 기반 파일명)
- ✅ 진행 상황 실시간 표시
- ✅ iframe 구조 자동 처리

## 설치

### 1. Python 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. Chrome WebDriver 설치

**자동 설치 (권장):**
```bash
pip install webdriver-manager
```

스크립트 수정:
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
self.driver = webdriver.Chrome(service=service, options=chrome_options)
```

**수동 설치:**
1. https://chromedriver.chromium.org/downloads 에서 Chrome 버전에 맞는 드라이버 다운로드
2. PATH에 추가하거나 스크립트와 같은 디렉토리에 배치

## 사용 방법

### 기본 실행
```bash
python naver_cafe_crawler.py
```

실행 후:
1. 네이버 카페 게시판 URL 입력
2. 이미지 저장 디렉토리 입력 (또는 Enter로 기본값 사용)

### 예시
```
네이버 카페 게시판 URL을 입력하세요: https://cafe.naver.com/f-e/cafes/30715281/menus/69
이미지 저장 디렉토리 (기본값: ./cafe_images): ./downloaded_images
```

## 커스터마이징

### 헤드리스 모드 (백그라운드 실행)
브라우저 창을 띄우지 않고 실행:
```python
chrome_options.add_argument('--headless')  # 주석 해제
```

### 이미 열려있는 Chrome 사용
로그인 상태를 유지하며 크롤링:

1. Chrome을 디버깅 모드로 실행:
```bash
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Windows  
chrome.exe --remote-debugging-port=9222
```

2. 스크립트에서 주석 해제:
```python
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
```

### 특정 페이지부터 시작
```python
crawler.crawl_from_oldest(start_page=10)  # 10페이지부터 시작
```

## 기술 스택

- **언어**: Python 3.x
- **웹 자동화**: Selenium WebDriver
- **HTTP 요청**: requests
- **브라우저**: Chrome/Chromium

## 프로젝트 구조

```
naver-cafe-crawler/
├── naver_cafe_crawler.py   # 메인 크롤러 스크립트
├── requirements.txt         # Python 의존성
├── README.md               # 이 문서
└── PROJECT.md              # 프로젝트 상세 문서
```

## 제약사항 및 주의사항

- 네이버 카페 이용약관 준수 필요
- 과도한 크롤링은 IP 차단의 원인이 될 수 있음
- 저작권이 있는 이미지는 개인적 용도로만 사용
- 로그인이 필요한 카페는 수동 로그인 또는 디버깅 모드 사용

## 문제 해결

### "Element not found" 오류
- 네이버 카페 HTML 구조 변경 가능성
- 로그인 필요 여부 확인
- `time.sleep()` 값 증가로 로딩 시간 확보

### "ChromeDriver" 오류
- ChromeDriver 설치 확인
- Chrome 브라우저와 ChromeDriver 버전 일치 확인

### iframe 관련 오류
- 네이버 카페는 iframe 사용
- `switch_to.frame()` 구현 확인

## 향후 개선 사항

- [ ] 멀티스레딩으로 다운로드 속도 개선
- [ ] 중복 이미지 검사 및 스킵 기능
- [ ] 다운로드 이력 관리 (JSON/SQLite)
- [ ] GUI 인터페이스 추가
- [ ] 동영상 다운로드 지원
- [ ] 첨부파일 다운로드 지원
- [ ] 재시작 기능 (중단된 위치부터 계속)

## 라이선스

개인 및 교육 목적으로 자유롭게 사용 가능합니다.

## 작성자

Seongwoo (eunsol)
