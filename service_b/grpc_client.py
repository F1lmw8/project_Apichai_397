import grpc
import os
import movie_pb2
import movie_pb2_grpc

# Get the gRPC server host from environment variable, default to localhost
GRPC_SERVER_HOST = os.getenv('GRPC_SERVER_HOST', 'localhost')
GRPC_SERVER_PORT = os.getenv('GRPC_SERVER_PORT', '50051')

# Create a function to fetch movie details from Service A (The Parent)
def get_movie_info(movie_id: int):
    target = f"{GRPC_SERVER_HOST}:{GRPC_SERVER_PORT}"
    print(f"Connecting to gRPC server at {target}")
    # Connect to the gRPC server
    with grpc.insecure_channel(target) as channel:
        stub = movie_pb2_grpc.MovieServiceStub(channel)
        
        request = movie_pb2.MovieRequest(movie_id=movie_id)
        try:
            response = stub.GetMovie(request)
            return {
                "title": response.title,
                "director": response.director,
                "year": response.year,
                "genre": response.genre
            }
        except grpc.RpcError as e:
            return {"error": e.details()}
