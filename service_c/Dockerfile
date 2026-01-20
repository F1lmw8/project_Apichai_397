FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from service_c to /app inside the container
COPY service_c /app

# Expose port (8002)
EXPOSE 8002

CMD ["python", "main.py"]
