#!/usr/bin/env python3
"""
네이버 카페 게시판 크롤러
- 게시판 목록을 오래된 순으로 탐색
- 게시글의 이미지를 다운로드
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
import os
from urllib.parse import urljoin, urlparse
from pathlib import Path
import json

class NaverCafeCrawler:
    def __init__(self, download_dir="./cafe_images"):
        """
        Args:
            download_dir: 이미지를 저장할 디렉토리
        """
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        
        # Chrome 옵션 설정
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # 백그라운드 실행 (필요시 활성화)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        # 이미 열려있는 Chrome에 연결하려면:
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def get_last_page_number(self):
        """게시판의 마지막 페이지 번호 찾기"""
        try:
            # 페이지네이션 영역 찾기
            pagination = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "prev-next"))
            )
            
            # 마지막 페이지 링크 찾기 (끝 버튼)
            last_button = pagination.find_element(By.CLASS_NAME, "pgR")
            last_page_url = last_button.get_attribute("href")
            
            # URL에서 페이지 번호 추출
            if "page=" in last_page_url:
                page_num = last_page_url.split("page=")[1].split("&")[0]
                return int(page_num)
            
            # 대안: 모든 페이지 번호에서 최대값 찾기
            page_numbers = pagination.find_elements(By.CLASS_NAME, "num")
            if page_numbers:
                max_page = max([int(p.text) for p in page_numbers if p.text.isdigit()])
                return max_page
                
        except Exception as e:
            print(f"마지막 페이지 찾기 실패: {e}")
            return 1
        
        return 1
    
    def go_to_page(self, page_number):
        """특정 페이지로 이동"""
        try:
            current_url = self.driver.current_url
            
            # URL 파싱 및 page 파라미터 추가/수정
            if "page=" in current_url:
                new_url = current_url.split("page=")[0] + f"page={page_number}"
            else:
                separator = "&" if "?" in current_url else "?"
                new_url = f"{current_url}{separator}page={page_number}"
            
            self.driver.get(new_url)
            time.sleep(2)  # 페이지 로딩 대기
            
            return True
        except Exception as e:
            print(f"페이지 이동 실패: {e}")
            return False
    
    def get_article_links(self):
        """현재 페이지의 모든 게시글 링크 수집"""
        try:
            # iframe으로 전환 (네이버 카페는 iframe 사용)
            self.driver.switch_to.frame("cafe_main")
            
            # 게시글 목록 찾기
            article_list = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "article-board"))
            )
            
            # 게시글 링크 수집
            articles = article_list.find_elements(By.CSS_SELECTOR, ".article-title a")
            links = []
            
            for article in articles:
                link = article.get_attribute("href")
                title = article.text
                if link:
                    links.append({"url": link, "title": title})
            
            # iframe에서 나오기
            self.driver.switch_to.default_content()
            
            return links
            
        except Exception as e:
            print(f"게시글 링크 수집 실패: {e}")
            self.driver.switch_to.default_content()
            return []
    
    def download_image(self, img_url, article_title, img_index):
        """이미지 다운로드"""
        try:
            # 파일명 생성 (제목 + 인덱스)
            safe_title = "".join(c for c in article_title if c.isalnum() or c in (' ', '-', '_'))[:50]
            ext = os.path.splitext(urlparse(img_url).path)[1] or '.jpg'
            filename = f"{safe_title}_{img_index}{ext}"
            filepath = self.download_dir / filename
            
            # 이미지 다운로드
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"  ✓ 다운로드 완료: {filename}")
            return True
            
        except Exception as e:
            print(f"  ✗ 이미지 다운로드 실패 ({img_url}): {e}")
            return False
    
    def process_article(self, article_url, article_title):
        """게시글 처리: 이미지 찾기 및 다운로드"""
        try:
            print(f"\n게시글: {article_title}")
            print(f"URL: {article_url}")
            
            self.driver.get(article_url)
            time.sleep(2)
            
            # iframe으로 전환
            self.driver.switch_to.frame("cafe_main")
            
            # 게시글 본문에서 이미지 찾기
            article_content = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "se-main-container"))
            )
            
            images = article_content.find_elements(By.TAG_NAME, "img")
            
            if not images:
                print("  이미지 없음")
                self.driver.switch_to.default_content()
                return
            
            print(f"  발견된 이미지: {len(images)}개")
            
            # 각 이미지 다운로드
            for idx, img in enumerate(images, 1):
                img_url = img.get_attribute("src")
                if img_url and img_url.startswith("http"):
                    self.download_image(img_url, article_title, idx)
            
            # iframe에서 나오기
            self.driver.switch_to.default_content()
            
        except Exception as e:
            print(f"게시글 처리 실패: {e}")
            self.driver.switch_to.default_content()
    
    def crawl_from_oldest(self, start_page=None):
        """오래된 순서대로 게시글 크롤링"""
        print("=" * 60)
        print("네이버 카페 크롤링 시작")
        print("=" * 60)
        
        # 마지막 페이지 번호 찾기
        if start_page is None:
            print("\n마지막 페이지 찾는 중...")
            last_page = self.get_last_page_number()
            print(f"마지막 페이지: {last_page}")
            start_page = last_page
        
        # 마지막 페이지부터 첫 페이지까지 순회
        for page in range(start_page, 0, -1):
            print(f"\n{'=' * 60}")
            print(f"페이지 {page} 처리 중...")
            print(f"{'=' * 60}")
            
            # 페이지 이동
            if not self.go_to_page(page):
                continue
            
            # 게시글 링크 수집
            articles = self.get_article_links()
            print(f"게시글 수: {len(articles)}개")
            
            # 각 게시글 처리 (오래된 순서)
            for article in articles:
                self.process_article(article["url"], article["title"])
                time.sleep(1)  # 서버 부하 방지
        
        print("\n" + "=" * 60)
        print("크롤링 완료!")
        print(f"이미지 저장 위치: {self.download_dir.absolute()}")
        print("=" * 60)
    
    def close(self):
        """브라우저 종료"""
        self.driver.quit()


def main():
    """메인 함수"""
    # 현재 열려있는 카페 URL 사용
    # 또는 특정 URL로 시작
    cafe_url = input("네이버 카페 게시판 URL을 입력하세요: ").strip()
    
    if not cafe_url:
        print("URL이 입력되지 않았습니다.")
        return
    
    download_dir = input("이미지 저장 디렉토리 (기본값: ./cafe_images): ").strip()
    if not download_dir:
        download_dir = "./cafe_images"
    
    # 크롤러 시작
    crawler = NaverCafeCrawler(download_dir=download_dir)
    
    try:
        # 카페 게시판 열기
        crawler.driver.get(cafe_url)
        time.sleep(3)  # 페이지 로딩 대기
        
        # 오래된 순서대로 크롤링
        crawler.crawl_from_oldest()
        
    except KeyboardInterrupt:
        print("\n\n사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n오류 발생: {e}")
    finally:
        crawler.close()


if __name__ == "__main__":
    main()
