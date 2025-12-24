"""
로또 번호 추천 모듈
분석 결과를 종합하여 로또 번호 추천
"""

import random
from typing import List, Dict, Optional, Set
from datetime import datetime
from .analyzer import LottoAnalyzer
from .database import Database


class LottoRecommender:
    """로또 번호 추천 클래스"""
    
    # 알고리즘 버전
    VERSION = "1.0.0"
    
    def __init__(self, db_path: str = "data/lotto.db"):
        """
        추천기 초기화
        
        Args:
            db_path: 데이터베이스 파일 경로
        """
        self.analyzer = LottoAnalyzer(db_path)
        self.db = Database(db_path)
        
        # 가중치 설정
        self.weights = {
            'frequency': 0.4,      # 출현 빈도
            'pattern': 0.3,        # 패턴 적합도
            'trend': 0.3           # 최근 추세
        }
    
    def _normalize_scores(self, scores: Dict[int, float]) -> Dict[int, float]:
        """
        점수 정규화 (0~1 범위)
        
        Args:
            scores: 원본 점수
            
        Returns:
            정규화된 점수
        """
        if not scores:
            return scores
        
        min_score = min(scores.values())
        max_score = max(scores.values())
        
        if max_score == min_score:
            return {num: 0.5 for num in scores}
        
        return {
            num: (score - min_score) / (max_score - min_score)
            for num, score in scores.items()
        }
    
    def _calc_frequency_score(self) -> Dict[int, float]:
        """
        출현 빈도 기반 점수 계산
        - 전체 빈도: 40%
        - 최근 50회: 30%
        - 최근 20회: 20%
        - 최근 10회: 10%
        
        Returns:
            번호별 빈도 점수
        """
        freq_all = self.analyzer.calculate_frequency()
        freq_50 = self.analyzer.calculate_frequency(recent_n=50)
        freq_20 = self.analyzer.calculate_frequency(recent_n=20)
        freq_10 = self.analyzer.calculate_frequency(recent_n=10)
        
        # 정규화
        norm_all = self._normalize_scores(freq_all)
        norm_50 = self._normalize_scores(freq_50)
        norm_20 = self._normalize_scores(freq_20)
        norm_10 = self._normalize_scores(freq_10)
        
        # 가중 평균
        scores = {}
        for num in range(1, 46):
            scores[num] = (
                norm_all[num] * 0.4 +
                norm_50[num] * 0.3 +
                norm_20[num] * 0.2 +
                norm_10[num] * 0.1
            )
        
        return scores
    
    def _calc_pattern_score(self) -> Dict[int, float]:
        """
        패턴 적합도 점수 계산
        - 홀짝 균형
        - 구간 분포 균형
        
        Returns:
            번호별 패턴 점수
        """
        patterns = self.analyzer.analyze_patterns(recent_n=100)
        
        # 기본 점수 0.5
        scores = {num: 0.5 for num in range(1, 46)}
        
        # 홀짝 균형 (3:3 선호)
        for num in range(1, 46):
            if num % 2 == 1:  # 홀수
                scores[num] += 0.1
            else:  # 짝수
                scores[num] += 0.1
        
        # 구간별 분포 (균형 선호)
        section_dist = patterns.get('section_distribution', {})
        total = sum(section_dist.values())
        
        if total > 0:
            for num in range(1, 46):
                section = self._get_section(num)
                section_ratio = section_dist.get(section, 0) / total
                
                # 과다 출현 구간은 감점, 과소 출현 구간은 가점
                if section_ratio > 0.25:  # 25% 이상
                    scores[num] -= 0.1
                elif section_ratio < 0.15:  # 15% 미만
                    scores[num] += 0.1
        
        return scores
    
    def _get_section(self, num: int) -> str:
        """번호의 구간 반환"""
        if 1 <= num <= 10:
            return '1-10'
        elif 11 <= num <= 20:
            return '11-20'
        elif 21 <= num <= 30:
            return '21-30'
        elif 31 <= num <= 40:
            return '31-40'
        else:
            return '41-45'
    
    def _calc_trend_score(self) -> Dict[int, float]:
        """
        최근 출현 추세 점수 계산
        
        Returns:
            번호별 추세 점수
        """
        trends = self.analyzer.analyze_recent_trend(window=20)
        
        scores = {}
        for num in range(1, 46):
            trend = trends.get(num, {})
            
            # 기본 점수
            score = 0.5
            
            # 최근 출현 여부
            recent_count = trend.get('recent_appearances', 0)
            
            if trend.get('is_hot'):  # 핫 넘버
                score += 0.3
            elif trend.get('is_cold'):  # 콜드 넘버
                score += 0.2  # 콜드넘버도 어느 정도 가점
            else:
                score += 0.1 * (recent_count / 20)  # 비례 점수
            
            scores[num] = score
        
        return scores
    
    def calculate_scores(self) -> Dict[int, float]:
        """
        각 번호의 종합 점수 계산
        
        Returns:
            번호별 종합 점수
        """
        # 각 요소별 점수 계산
        freq_scores = self._calc_frequency_score()
        pattern_scores = self._calc_pattern_score()
        trend_scores = self._calc_trend_score()
        
        # 종합 점수
        total_scores = {}
        for num in range(1, 46):
            total_scores[num] = (
                freq_scores[num] * self.weights['frequency'] +
                pattern_scores[num] * self.weights['pattern'] +
                trend_scores[num] * self.weights['trend']
            )
        
        return total_scores
    
    def recommend(
        self, 
        count: int = 6,
        exclude: Optional[List[int]] = None,
        include: Optional[List[int]] = None
    ) -> List[int]:
        """
        번호 추천
        
        Args:
            count: 추천할 번호 개수 (기본: 6)
            exclude: 제외할 번호 리스트
            include: 반드시 포함할 번호 리스트
            
        Returns:
            추천 번호 리스트 (오름차순)
        """
        if exclude is None:
            exclude = []
        if include is None:
            include = []
        
        # 입력 검증
        if not (1 <= count <= 6):
            raise ValueError("추천 번호는 1~6개여야 합니다")
        
        if len(include) > count:
            raise ValueError("포함 번호가 추천 개수보다 많습니다")
        
        # 종합 점수 계산
        scores = self.calculate_scores()
        
        # 제외 번호 제거
        for num in exclude:
            if num in scores:
                del scores[num]
        
        # 포함 번호 제거 (이미 선택됨)
        for num in include:
            if num in scores:
                del scores[num]
        
        # 필요한 번호 개수
        needed = count - len(include)
        
        # 상위 점수 번호 선택 (약간의 랜덤성 추가)
        candidates = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # 상위 20개 중에서 확률적으로 선택 (다양성 증가)
        top_candidates = candidates[:min(20, len(candidates))]
        weights = [score for _, score in top_candidates]
        
        selected = random.choices(
            [num for num, _ in top_candidates],
            weights=weights,
            k=needed
        )
        
        # 최종 번호 (포함 번호 + 선택 번호)
        final_numbers = sorted(list(set(include + selected)))
        
        return final_numbers[:count]
    
    def recommend_multiple(
        self, 
        sets: int = 5,
        exclude: Optional[List[int]] = None,
        include: Optional[List[int]] = None
    ) -> List[List[int]]:
        """
        여러 조합 추천
        
        Args:
            sets: 추천할 조합 개수
            exclude: 제외할 번호 리스트
            include: 반드시 포함할 번호 리스트
            
        Returns:
            추천 번호 조합 리스트
        """
        recommendations = []
        seen_combinations: Set[tuple] = set()
        
        max_attempts = sets * 10  # 무한 루프 방지
        attempts = 0
        
        while len(recommendations) < sets and attempts < max_attempts:
            numbers = self.recommend(
                count=6,
                exclude=exclude,
                include=include
            )
            
            numbers_tuple = tuple(numbers)
            if numbers_tuple not in seen_combinations:
                recommendations.append(numbers)
                seen_combinations.add(numbers_tuple)
            
            attempts += 1
        
        return recommendations
    
    def save_recommendation(
        self, 
        numbers: List[int],
        confidence: float = 0.0,
        notes: str = ""
    ) -> bool:
        """
        추천 결과 저장
        
        Args:
            numbers: 추천 번호
            confidence: 신뢰도 점수
            notes: 메모
            
        Returns:
            성공 여부
        """
        if len(numbers) != 6:
            return False
        
        try:
            with self.db as db:
                db.execute("""
                    INSERT INTO recommendations
                    (num1, num2, num3, num4, num5, num6, 
                     algorithm_version, confidence_score, notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    numbers[0], numbers[1], numbers[2],
                    numbers[3], numbers[4], numbers[5],
                    self.VERSION, confidence, notes
                ))
            return True
        except Exception as e:
            print(f"❌ 추천 저장 실패: {e}")
            return False


if __name__ == "__main__":
    # 추천기 테스트
    recommender = LottoRecommender()
    
    # 단일 추천
    numbers = recommender.recommend()
    print(f"추천 번호: {numbers}")
    
    # 여러 조합 추천
    multiple = recommender.recommend_multiple(sets=5)
    print(f"\n5개 조합 추천:")
    for i, nums in enumerate(multiple, 1):
        print(f"{i}. {nums}")
