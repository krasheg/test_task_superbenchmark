from typing import List, Dict
from config import DEBUG_MODE, SessionLocal
from fastapi import HTTPException
from models import BenchmarkResult
import json


def get_data() -> List[Dict]:
    """
    Load benchmarking results from either JSON file (DEBUG mode) or PostgreSQL.
    """
    if DEBUG_MODE:
        session = SessionLocal()
        try:
            results = session.query(BenchmarkResult).all()
            return [result.__dict__ for result in results]
        finally:
            session.close()
    else:
        print('Debug mode is:', DEBUG_MODE)
        raise Exception("Feature is not ready for live yet")
