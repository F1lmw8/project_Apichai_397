FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from service_a to /app inside the container
COPY service_a /app

# Expose ports for FastAPI (8000) and gRPC (50051)
EXPOSE 8000 50051

CMD ["python", "main.py"]
