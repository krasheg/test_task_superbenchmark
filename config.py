import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Check if DEBUG mode is enabled based on the environment variable
print('Debug from env is: ', os.environ.get('SUPERBENCHMARK_DEBUG'))
DEBUG_MODE: bool = os.getenv("SUPERBENCHMARK_DEBUG", "true").lower() == "true"
# Set up the database URL and connection if DEBUG is False
DATABASE_URL = os.getenv("DATABASE_URL",
                         'postgresql://superbenchmark_user:superbenchmark_password@db:5432/superbenchmark_db')
engine = create_engine(DATABASE_URL) if DEBUG_MODE else None
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
