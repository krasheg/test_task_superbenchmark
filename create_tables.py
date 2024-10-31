from sqlalchemy import inspect

from config import engine, Base, DEBUG_MODE
from models import BenchmarkResult
from sqlalchemy.orm import Session
import json


def create_tables() -> None:
    """Create database tables if they do not exist."""
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if not tables:
        # Create tables if they do not exist
        Base.metadata.create_all(engine)
        print("Tables created successfully")
    else:
        print("Tables already exist")


def load_data_from_json(session: Session, file_path: str = "test_database.json") -> None:
    """Load initial data from JSON file into the database if table is empty."""
    if not DEBUG_MODE:  # Checking DEBUG mode
        print('Debug mode is:', DEBUG_MODE)
        return

    # Check if the table is empty
    if not session.query(BenchmarkResult).first():
        with open(file_path, "r") as f:
            data = json.load(f).get("benchmarking_results", [])  # Use correct key
            # Add each benchmarking result from JSON into the database
            for item in data:
                result = BenchmarkResult(
                    request_id=item["request_id"],
                    prompt_text=item["prompt_text"],
                    generated_text=item["generated_text"],
                    token_count=item["token_count"],
                    time_to_first_token=item["time_to_first_token"],
                    time_per_output_token=item["time_per_output_token"],
                    total_generation_time=item["total_generation_time"],
                    timestamp=item["timestamp"],
                )
                session.add(result)
            session.commit()


if __name__ == "__main__":
    create_tables()
    # Initialize a new session for data loading
    with Session(engine) as new_session:
        load_data_from_json(new_session)
