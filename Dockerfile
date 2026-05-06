# Use a modern, supported Python image (Bookworm is the latest stable Debian)
FROM python:3.10-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt update -y && apt-get update && pip install -r requirements.txt

# Retrain the model inside the container to guarantee 100% pickle and scikit-learn compatibility
ENV PYTHONPATH=/app
RUN python3 -m src.components.data_ingestion

# Run the application
CMD ["python3", "app.py"]
