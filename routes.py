from fastapi import APIRouter, HTTPException
from typing import Dict
from database import get_data
from dateutil import parser
router = APIRouter()
data = get_data()


@router.get("/results/average")
def get_average_results() -> Dict[str, float]:
    """
    Endpoint to calculate and return the average performance statistics for all results.
    """
    token_counts = [item["token_count"] for item in data]
    average_token_count = sum(token_counts) / len(token_counts) if token_counts else 0
    return {"average_token_count": average_token_count}


@router.get("/results/average/{start_time}/{end_time}")
def get_average_results_in_time_window(start_time: str, end_time: str) -> Dict[str, float]:
    """
    Endpoint to calculate average performance statistics for results within a given time window.
    """
    try:
        start = parser.parse(start_time)
        end = parser.parse(end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format")

    filtered_results = [
        item for item in data
        if start <= item["timestamp"] <= end
    ]
    token_counts = [item["token_count"] for item in filtered_results]
    average_token_count = sum(token_counts) / len(token_counts) if token_counts else 0
    return {"average_token_count": average_token_count}
