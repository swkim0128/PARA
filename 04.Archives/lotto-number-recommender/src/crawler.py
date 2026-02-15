"""
로또 데이터 크롤러 모듈
동행복권 API를 통해 로또 당첨 번호 데이터를 수집
"""

import requests
import time
from typing import Optional, Dict, Any
from datetime import datetime
from .database import Database


class LottoCrawler:
    """로또 데이터 크롤러 클래스"""
    
    API_URL = "https://www.dhlottery.co.kr/common.do"
    
    def __init__(self, db_path: str = "data/lotto.db"):
        """
        크롤러 초기화
        
        Args:
            db_path: 데이터베이스 파일 경로
        """
        self.db = Database(db_path)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        })
    
    def get_latest_round_from_api(self) -> Optional[int]:
        """
        API에서 현재 최신 회차 번호 가져오기
        
        Returns:
            최신 회차 번호 또는 None
        """
        try:
            # 충분히 큰 회차 번호로 요청하면 최신 회차를 반환
            response = self.fetch_lotto_data(10000)
            if response:
                return response.get('round')
            return None
        except Exception as e:
            print(f"❌ 최신 회차 조회 실패: {e}")
            return None
    
    def fetch_lotto_data(self, round_num: int) -> Optional[Dict[str, Any]]:
        """
        특정 회차의 로또 데이터 가져오기
        
        Args:
            round_num: 회차 번호
            
        Returns:
            로또 데이터 딕셔너리 또는 None
        """
        try:
            params = {
                'method': 'getLottoNumber',
                'drwNo': round_num
            }
            
            response = self.session.get(self.API_URL, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # API 응답 검증
            if data.get('returnValue') != 'success':
                return None
            
            # 데이터 파싱
            lotto_data = {
                'round': data['drwNo'],
                'draw_date': data['drwNoDate'],
                'num1': data['drwtNo1'],
                'num2': data['drwtNo2'],
                'num3': data['drwtNo3'],
                'num4': data['drwtNo4'],
                'num5': data['drwtNo5'],
                'num6': data['drwtNo6'],
                'bonus_num': data['bnusNo'],
                'first_prize': data.get('firstWinamnt'),
                'first_winner_count': data.get('firstPrzwnerCo')
            }
            
            return lotto_data
            
        except requests.RequestException as e:
            print(f"❌ API 요청 실패 (회차 {round_num}): {e}")
            return None
        except (KeyError, ValueError) as e:
            print(f"❌ 데이터 파싱 실패 (회차 {round_num}): {e}")
            return None
    
    def save_to_db(self, data: Dict[str, Any]) -> bool:
        """
        데이터베이스에 저장
        
        Args:
            data: 로또 데이터
            
        Returns:
            성공 여부
        """
        with self.db as db:
            return db.insert_lotto_result(data)
    
    def crawl_all(self, start_round: int = 1, delay: float = 0.5) -> int:
        """
        초기 데이터 수집 (1회차부터 최신까지)
        
        Args:
            start_round: 시작 회차 (기본: 1)
            delay: 요청 간 딜레이 (초)
            
        Returns:
            수집한 회차 수
        """
        print(f"🔍 로또 데이터 수집 시작 (회차 {start_round}부터)")
        
        # 최신 회차 확인
        latest_round = self.get_latest_round_from_api()
        if not latest_round:
            print("❌ 최신 회차를 확인할 수 없습니다.")
            return 0
        
        print(f"📊 최신 회차: {latest_round}")
        
        collected_count = 0
        failed_rounds = []
        
        for round_num in range(start_round, latest_round + 1):
            print(f"📥 회차 {round_num} 수집 중... ", end='', flush=True)
            
            data = self.fetch_lotto_data(round_num)
            if data and self.save_to_db(data):
                print("✅")
                collected_count += 1
            else:
                print("❌")
                failed_rounds.append(round_num)
            
            # Rate limiting 방지
            time.sleep(delay)
        
        print(f"\n✅ 수집 완료: {collected_count}/{latest_round - start_round + 1} 회차")
        
        if failed_rounds:
            print(f"❌ 실패한 회차: {failed_rounds}")
        
        return collected_count
    
    def update_latest(self, delay: float = 0.5) -> bool:
        """
        최신 회차 데이터만 업데이트
        
        Args:
            delay: 요청 간 딜레이 (초)
            
        Returns:
            성공 여부
        """
        print("🔄 최신 데이터 업데이트 시작")
        
        # DB의 최신 회차
        with self.db as db:
            db_latest = db.get_latest_round()
        
        if db_latest is None:
            print("⚠️  DB가 비어있습니다. crawl_all()을 먼저 실행하세요.")
            return False
        
        # API의 최신 회차
        api_latest = self.get_latest_round_from_api()
        if not api_latest:
            print("❌ 최신 회차를 확인할 수 없습니다.")
            return False
        
        if db_latest >= api_latest:
            print(f"✅ 이미 최신 상태입니다. (회차 {db_latest})")
            return True
        
        # 누락된 회차 수집
        print(f"📊 수집할 회차: {db_latest + 1} ~ {api_latest}")
        
        collected = []
        for round_num in range(db_latest + 1, api_latest + 1):
            print(f"📥 회차 {round_num} 수집 중... ", end='', flush=True)
            
            data = self.fetch_lotto_data(round_num)
            if data and self.save_to_db(data):
                print("✅")
                collected.append(round_num)
            else:
                print("❌")
            
            time.sleep(delay)
        
        if collected:
            print(f"✅ {len(collected)}개 회차 업데이트 완료")
            return True
        else:
            print("❌ 업데이트 실패")
            return False


if __name__ == "__main__":
    # 크롤러 테스트
    crawler = LottoCrawler()
    
    # 최신 회차 확인
    latest = crawler.get_latest_round_from_api()
    print(f"최신 회차: {latest}")
    
    # 특정 회차 데이터 가져오기
    data = crawler.fetch_lotto_data(1)
    if data:
        print(f"1회차 데이터: {data}")
