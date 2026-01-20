from fastapi import FastAPI, HTTPException
from grpc_client import get_movie_info

app = FastAPI()

@app.get("/")
def read_root():
    # หน้าแรกสำหรับแนะนำเส้นทาง (Index Page)
    return {
        "message": "Welcome to Service B (Child of Movie Service)",
        "description": "Service B เปรียบเสมือน Class ลูก ที่สืบทอดคุณสมบัติมาจาก Service A",
        "available_endpoints": [
            "/my-movie (The Matrix) - ดูหนังประจำตัวของ Service B",
            "/movie/{id} (Fetch by ID) - ดูหนังเรื่องอื่นๆ โดยดึงจาก Service A"
        ]
    }

@app.get("/movie/{movie_id}")
def read_movie(movie_id: int):
    movie_info = get_movie_info(movie_id)

    if "error" in movie_info:
        raise HTTPException(status_code=404, detail=movie_info["error"])
    
    return {
        "fetched_by": "Service B (Child)",
        "inheritance_info": "This data is INHERITED from Service A (Parent/Base Class)",
        "data_source": "Service A gRPC Server",
        "movie_data": movie_info
    }

@app.get("/my-movie")
def get_my_movie():
    # Service B represents "The Matrix" (ID 8)
    # Service B ทำหน้าที่เป็นคลูก (Child Class) ที่เฉพาะเจาะจงว่าเป็นหนังเรื่อง "The Matrix"
    # โดยการ "Inherit" (ดึงข้อมูล) มาจาก Service A (Parent Class)
    movie_info = get_movie_info(8)
    return {
        "fetched_by": "Service B (The Matrix)",
        "inheritance_info": "I am specifically 'The Matrix', but my data comes from Service A",
        "inheritance_description": "Service B สืบทอดข้อมูลมาจาก Service A (Class A)",
        "movie_data": movie_info
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
