import grpc
from concurrent import futures
import time

# Import the generated classes
import movie_pb2_grpc
import movie_pb2

# Class A: Base Data Provider (คลาสแม่: ผู้ให้บริการข้อมูลหลัก)
class MovieBase:
    def __init__(self):
        # Database ของหนัง (เปรียบเสมือน Property ของคลาสแม่)
        self.movie_db = {
            1: {"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994, "genre": "Drama"},
            2: {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "genre": "Crime"},
            3: {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "genre": "Action"},
            4: {"title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994, "genre": "Crime"},
            5: {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "genre": "Sci-Fi"},
            6: {"title": "Titanic", "director": "James Cameron", "year": 1997, "genre": "Romance"},
            7: {"title": "Avatar", "director": "James Cameron", "year": 2009, "genre": "Sci-Fi"},
            8: {"title": "The Matrix", "director": "The Wachowskis", "year": 1999, "genre": "Sci-Fi"},
            9: {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "genre": "Sci-Fi"},
            10: {"title": "Parasite", "director": "Bong Joon-ho", "year": 2019, "genre": "Thriller"},
        }
    
    def get_movie(self, movie_id):
        # ฟังก์ชันสำหรับดึงข้อมูลหนัง (Method ของคลาสแม่)
        return self.movie_db.get(movie_id)

# Initialize the base data
base_data = MovieBase()

# Create a class to define the server functions, inheriting from generated class
# คลาสนี้ทำหน้าที่เปิดช่องทาง (Interface) ให้ลูกๆ (Service B/C) เข้ามาเรียกใช้ข้อมูลได้
class MovieServiceServicer(movie_pb2_grpc.MovieServiceServicer):

    def GetMovie(self, request, context):
        movie_id = request.movie_id
        # เรียกใช้ข้อมูลจาก Class แม่ (MovieBase)
        movie = base_data.get_movie(movie_id)

        if movie:
            return movie_pb2.MovieReply(
                title=movie["title"],
                director=movie["director"],
                year=movie["year"],
                genre=movie["genre"]
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Movie with ID {movie_id} not found.")
            return movie_pb2.MovieReply()

# Start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServiceServicer_to_server(MovieServiceServicer(), server)

    server.add_insecure_port('[::]:50051')
    print("Starting Movie gRPC server on port 50051...")
    server.start()
    server.wait_for_termination()
