"""
로또 데이터 분석 모듈
수집된 로또 데이터를 분석하여 통계, 패턴, 추세 등을 계산
"""

from typing import Dict, List, Optional, Tuple
from collections import Counter
from .database import Database


class LottoAnalyzer:
    """로또 데이터 분석 클래스"""
    
    def __init__(self, db_path: str = "data/lotto.db"):
        """
        분석기 초기화
        
        Args:
            db_path: 데이터베이스 파일 경로
        """
        self.db = Database(db_path)
    
    def calculate_frequency(self, recent_n: Optional[int] = None) -> Dict[int, int]:
        """
        번호별 출현 빈도 계산
        
        Args:
            recent_n: 최근 N회차만 분석 (None이면 전체)
            
        Returns:
            {번호: 출현횟수} 딕셔너리
        """
        with self.db as db:
            if recent_n:
                query = """
                    SELECT num1, num2, num3, num4, num5, num6
                    FROM lotto_results
                    ORDER BY round DESC
                    LIMIT ?
                """
                results = db.fetchall(query, (recent_n,))
            else:
                query = """
                    SELECT num1, num2, num3, num4, num5, num6
                    FROM lotto_results
                """
                results = db.fetchall(query)
        
        # 모든 번호 수집
        all_numbers = []
        for row in results:
            all_numbers.extend([
                row['num1'], row['num2'], row['num3'],
                row['num4'], row['num5'], row['num6']
            ])
        
        # 빈도 계산
        frequency = Counter(all_numbers)
        
        # 1~45까지 모든 번호 포함 (출현하지 않은 번호는 0)
        return {num: frequency.get(num, 0) for num in range(1, 46)}
    
    def analyze_patterns(self, recent_n: int = 100) -> Dict[str, any]:
        """
        패턴 분석
        - 연속 번호 출현 비율
        - 홀짝 비율
        - 구간별 분포
        
        Args:
            recent_n: 최근 N회차 분석
            
        Returns:
            패턴 분석 결과
        """
        with self.db as db:
            query = """
                SELECT num1, num2, num3, num4, num5, num6
                FROM lotto_results
                ORDER BY round DESC
                LIMIT ?
            """
            results = db.fetchall(query, (recent_n,))
        
        consecutive_count = 0
        odd_even_ratios = []
        section_distributions = {
            '1-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-45': 0
        }
        
        for row in results:
            numbers = sorted([
                row['num1'], row['num2'], row['num3'],
                row['num4'], row['num5'], row['num6']
            ])
            
            # 연속 번호 체크
            has_consecutive = False
            for i in range(len(numbers) - 1):
                if numbers[i+1] - numbers[i] == 1:
                    has_consecutive = True
                    break
            if has_consecutive:
                consecutive_count += 1
            
            # 홀짝 비율
            odd_count = sum(1 for n in numbers if n % 2 == 1)
            odd_even_ratios.append(f"{odd_count}:{6-odd_count}")
            
            # 구간별 분포
            for num in numbers:
                if 1 <= num <= 10:
                    section_distributions['1-10'] += 1
                elif 11 <= num <= 20:
                    section_distributions['11-20'] += 1
                elif 21 <= num <= 30:
                    section_distributions['21-30'] += 1
                elif 31 <= num <= 40:
                    section_distributions['31-40'] += 1
                else:
                    section_distributions['41-45'] += 1
        
        return {
            'consecutive_rate': consecutive_count / len(results) if results else 0,
            'most_common_odd_even': Counter(odd_even_ratios).most_common(3),
            'section_distribution': section_distributions,
            'total_analyzed': len(results)
        }
    
    def analyze_recent_trend(self, window: int = 10) -> Dict[int, Dict[str, any]]:
        """
        최근 출현 추세 분석
        
        Args:
            window: 분석 윈도우 (회차)
            
        Returns:
            번호별 추세 정보
        """
        with self.db as db:
            query = """
                SELECT round, num1, num2, num3, num4, num5, num6
                FROM lotto_results
                ORDER BY round DESC
                LIMIT ?
            """
            results = db.fetchall(query, (window,))
        
        # 번호별 최근 출현 정보
        number_trends = {}
        
        for num in range(1, 46):
            appearances = []
            for row in results:
                numbers = [
                    row['num1'], row['num2'], row['num3'],
                    row['num4'], row['num5'], row['num6']
                ]
                if num in numbers:
                    appearances.append(row['round'])
            
            # 추세 계산
            trend_info = {
                'recent_appearances': len(appearances),
                'last_appearance': max(appearances) if appearances else None,
                'is_hot': len(appearances) >= window * 0.2,  # 20% 이상 출현
                'is_cold': len(appearances) == 0  # 미출현
            }
            
            number_trends[num] = trend_info
        
        return number_trends
    
    def get_cold_numbers(self, threshold: int = 10) -> List[int]:
        """
        오랫동안 미출현한 번호 찾기
        
        Args:
            threshold: 미출현 회차 기준
            
        Returns:
            콜드 번호 리스트
        """
        with self.db as db:
            latest_round = db.get_latest_round()
            if not latest_round:
                return []
        
        cold_numbers = []
        
        with self.db as db:
            for num in range(1, 46):
                query = """
                    SELECT MAX(round) as last_round
                    FROM lotto_results
                    WHERE num1 = ? OR num2 = ? OR num3 = ? 
                       OR num4 = ? OR num5 = ? OR num6 = ?
                """
                result = db.fetchone(query, (num, num, num, num, num, num))
                
                last_round = result['last_round'] if result else None
                
                if last_round is None or (latest_round - last_round) >= threshold:
                    cold_numbers.append(num)
        
        return sorted(cold_numbers)
    
    def get_hot_numbers(self, recent_n: int = 10, top_k: int = 10) -> List[Tuple[int, int]]:
        """
        최근 자주 출현한 번호 찾기
        
        Args:
            recent_n: 최근 N회차
            top_k: 상위 K개
            
        Returns:
            [(번호, 출현횟수)] 리스트
        """
        frequency = self.calculate_frequency(recent_n=recent_n)
        hot_numbers = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return hot_numbers[:top_k]
    
    def get_statistics_summary(self) -> Dict[str, any]:
        """
        전체 통계 요약
        
        Returns:
            통계 요약 정보
        """
        with self.db as db:
            total_rounds = db.fetchone("SELECT COUNT(*) as count FROM lotto_results")
            latest_round = db.get_latest_round()
            
            if not total_rounds or total_rounds['count'] == 0:
                return {'error': '데이터가 없습니다'}
        
        frequency_all = self.calculate_frequency()
        frequency_recent = self.calculate_frequency(recent_n=50)
        patterns = self.analyze_patterns(recent_n=100)
        hot_numbers = self.get_hot_numbers(recent_n=20, top_k=10)
        cold_numbers = self.get_cold_numbers(threshold=10)
        
        return {
            'total_rounds': total_rounds['count'],
            'latest_round': latest_round,
            'most_frequent_all': sorted(frequency_all.items(), 
                                       key=lambda x: x[1], reverse=True)[:10],
            'most_frequent_recent': sorted(frequency_recent.items(), 
                                          key=lambda x: x[1], reverse=True)[:10],
            'patterns': patterns,
            'hot_numbers': hot_numbers,
            'cold_numbers': cold_numbers
        }


if __name__ == "__main__":
    # 분석기 테스트
    analyzer = LottoAnalyzer()
    
    # 전체 빈도 분석
    freq = analyzer.calculate_frequency()
    print(f"전체 빈도 (상위 10개): {sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]}")
    
    # 통계 요약
    summary = analyzer.get_statistics_summary()
    print(f"\n통계 요약:\n{summary}")
