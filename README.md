# SuperBenchmark

SuperBenchmark is a FastAPI application that manages and queries benchmarking results for a Large Language Model (LLM).

## Features

- **GET /results/average** - Returns average performance statistics across all benchmarking results.
- **GET /results/average/{start_time}/{end_time}** - Returns average performance statistics within a specified time window.

## Project Setup

1. **Configuration**:
   - `SUPERBENCHMARK_DEBUG`: Set to `True` to read data from `PostgreSQL` or `False` to raise exception.
   - `DATABASE_URL`: Connection string for PostgreSQL (required when `SUPERBENCHMARK_DEBUG=True`).

2. **Local Setup**:
   - Ensure you have Docker installed.
   - create `.env` file
     ```bash
     cp .env_template .env

3. **Run Project**:

   - Start the application:
     ```bash
     docker-compose --env-file .env  up -d --build
     ```

4. **Endpoints**:
   - `/results/average` - Returns the average token count.
   - `/results/average/{start_time}/{end_time}` - Returns the average token count within a specified time window.

5. **File Structure**:
   - `config.py`: Configuration for environment variables and database connection.
   - `models.py`: Data model for the benchmarking result.
   - `database.py`: Data access logic for JSON and PostgreSQL.
   - `routes.py`: API endpoints for querying data.
   - `main.py`: FastAPI application initialization.
   - `create_tables.py`: Script to create database tables.
   - `wait-for-it.sh`: Bash cript that ensure that DB is already started.
   - `entrypoint.sh`: Bash ccript that create database tables, add data and start the application.

6. **Testing with Debug Mode**:
   - To test locally, set `SUPERBENCHMARK_DEBUG=True` and add sample data to `test_database.json`.


