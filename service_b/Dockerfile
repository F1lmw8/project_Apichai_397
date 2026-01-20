FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from service_b to /app inside the container
COPY service_b /app

# Expose port (8001)
EXPOSE 8001

CMD ["python", "main.py"]
