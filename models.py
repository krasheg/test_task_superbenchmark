from sqlalchemy import Column, Integer, String, DateTime
from config import Base
from datetime import datetime


class BenchmarkResult(Base):
    """Data model for storing benchmarking results."""
    __tablename__ = "benchmark_results"

    request_id: str = Column(String, primary_key=True, index=True)
    prompt_text: str = Column(String, nullable=False)
    generated_text: str = Column(String, nullable=False)
    token_count: int = Column(Integer, nullable=False)
    time_to_first_token: int = Column(Integer, nullable=False)
    time_per_output_token: int = Column(Integer, nullable=False)
    total_generation_time: int = Column(Integer, nullable=False)
    timestamp: datetime = Column(DateTime, nullable=False)
