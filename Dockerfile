# Use the official Python image
FROM python:3.10-slim

# Set environment variables for optimal container behavior
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies for PostgreSQL support
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Copy files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENTRYPOINT ["/entrypoint.sh"]
