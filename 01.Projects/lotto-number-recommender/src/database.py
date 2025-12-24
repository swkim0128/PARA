"""
데이터베이스 관리 모듈
SQLite 데이터베이스 초기화, 연결, 쿼리 실행 등을 담당
"""

import sqlite3
from typing import Optional, List, Dict, Any
from datetime import datetime
import os


class Database:
    """로또 데이터베이스 관리 클래스"""
    
    def __init__(self, db_path: str = "data/lotto.db"):
        """
        데이터베이스 초기화
        
        Args:
            db_path: 데이터베이스 파일 경로
        """
        self.db_path = db_path
        self._ensure_db_directory()
        self.conn: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None
        
    def _ensure_db_directory(self):
        """데이터베이스 디렉토리 생성"""
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
    
    def connect(self):
        """데이터베이스 연결"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # dict-like access
        self.cursor = self.conn.cursor()
        
    def disconnect(self):
        """데이터베이스 연결 종료"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    
    def __enter__(self):
        """Context manager 진입"""
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager 종료"""
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.disconnect()
    
    def initialize_schema(self):
        """데이터베이스 스키마 초기화"""
        self.connect()
        
        # lotto_results 테이블
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS lotto_results (
                round INTEGER PRIMARY KEY,
                draw_date DATE NOT NULL,
                num1 INTEGER NOT NULL CHECK(num1 BETWEEN 1 AND 45),
                num2 INTEGER NOT NULL CHECK(num2 BETWEEN 1 AND 45),
                num3 INTEGER NOT NULL CHECK(num3 BETWEEN 1 AND 45),
                num4 INTEGER NOT NULL CHECK(num4 BETWEEN 1 AND 45),
                num5 INTEGER NOT NULL CHECK(num5 BETWEEN 1 AND 45),
                num6 INTEGER NOT NULL CHECK(num6 BETWEEN 1 AND 45),
                bonus_num INTEGER NOT NULL CHECK(bonus_num BETWEEN 1 AND 45),
                first_prize BIGINT,
                first_winner_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(num1, num2, num3, num4, num5, num6)
            )
        """)
        
        # 인덱스 생성
        self.cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_draw_date 
            ON lotto_results(draw_date)
        """)
        
        self.cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_round 
            ON lotto_results(round DESC)
        """)
        
        # number_frequency 테이블
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS number_frequency (
                number INTEGER PRIMARY KEY CHECK(number BETWEEN 1 AND 45),
                total_count INTEGER DEFAULT 0,
                recent_10_count INTEGER DEFAULT 0,
                recent_20_count INTEGER DEFAULT 0,
                recent_50_count INTEGER DEFAULT 0,
                last_appeared_round INTEGER,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # recommendations 테이블
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recommendations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recommended_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                num1 INTEGER, num2 INTEGER, num3 INTEGER,
                num4 INTEGER, num5 INTEGER, num6 INTEGER,
                algorithm_version VARCHAR(20),
                confidence_score FLOAT,
                notes TEXT
            )
        """)
        
        self.conn.commit()
        self.disconnect()
        
        print("✅ 데이터베이스 스키마 초기화 완료")
    
    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """
        SQL 쿼리 실행
        
        Args:
            query: SQL 쿼리문
            params: 쿼리 파라미터
            
        Returns:
            Cursor 객체
        """
        return self.cursor.execute(query, params)
    
    def fetchone(self, query: str, params: tuple = ()) -> Optional[Dict[str, Any]]:
        """
        단일 행 조회
        
        Args:
            query: SQL 쿼리문
            params: 쿼리 파라미터
            
        Returns:
            조회 결과 (dict) 또는 None
        """
        self.execute(query, params)
        row = self.cursor.fetchone()
        return dict(row) if row else None
    
    def fetchall(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """
        모든 행 조회
        
        Args:
            query: SQL 쿼리문
            params: 쿼리 파라미터
            
        Returns:
            조회 결과 리스트
        """
        self.execute(query, params)
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]
    
    def get_latest_round(self) -> Optional[int]:
        """
        데이터베이스에 저장된 최신 회차 반환
        
        Returns:
            최신 회차 번호 또는 None
        """
        result = self.fetchone("SELECT MAX(round) as max_round FROM lotto_results")
        return result['max_round'] if result else None
    
    def insert_lotto_result(self, data: Dict[str, Any]) -> bool:
        """
        로또 당첨 결과 저장
        
        Args:
            data: 로또 데이터 딕셔너리
            
        Returns:
            성공 여부
        """
        try:
            self.execute("""
                INSERT OR REPLACE INTO lotto_results 
                (round, draw_date, num1, num2, num3, num4, num5, num6, 
                 bonus_num, first_prize, first_winner_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data['round'],
                data['draw_date'],
                data['num1'], data['num2'], data['num3'],
                data['num4'], data['num5'], data['num6'],
                data['bonus_num'],
                data.get('first_prize'),
                data.get('first_winner_count')
            ))
            return True
        except Exception as e:
            print(f"❌ 데이터 저장 실패: {e}")
            return False


if __name__ == "__main__":
    # 데이터베이스 초기화 테스트
    db = Database()
    db.initialize_schema()
