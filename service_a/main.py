import threading
import uvicorn
from fastapi import FastAPI

from grpc_server import serve  # Import the gRPC server function

# Create FastAPI app
app = FastAPI()

# Simple health check route
@app.get("/")
def read_root():
    return {"message": "FastAPI is running alongside gRPC server!"}

# Function to run gRPC server in a separate thread
def start_grpc_server():
    serve()

if __name__ == "__main__":
    # Start gRPC server in a separate thread
    grpc_thread = threading.Thread(target=start_grpc_server, daemon=True)
    grpc_thread.start()

    # Start FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000)
