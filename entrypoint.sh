#!/bin/bash

set -e

./wait-for-it.sh db:5432 --

python create_tables.py

exec uvicorn main:app --host 0.0.0.0 --port 8000
