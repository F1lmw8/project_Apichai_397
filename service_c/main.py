from fastapi import FastAPI, HTTPException
from grpc_client import get_movie_info

app = FastAPI()

@app.get("/")
def read_root():
    # Service C: อีกหนึ่งตัวอย่าง Class ลูก
    return {
        "message": "Hello from Service C (Child C) - I can also fetch movies!",
        "description": "Service C ก็เป็น Child Class ของ Service A เช่นกัน แต่เป็นหนังคนละเรื่อง (Polymorphism)",
        "available_endpoints": ["/my-movie (Titanic)", "/movie-details/{id}"]
    }

@app.get("/movie-details/{movie_id}")
def read_movie_details(movie_id: int):
    # Service C might process it differently or just pass it through
    data = get_movie_info(movie_id)
    if "error" in data:
         raise HTTPException(status_code=404, detail=data["error"])
    return {
        "fetched_by": "Service C (Child)",
        "inheritance_info": "This data is INHERITED from Service A (Parent/Base Class)",
        "data_source": "Service A gRPC Server",
        "movie_data": data
    }

@app.get("/my-movie")
def get_my_movie():
    # Service C represents "Titanic" (ID 6)
    # Service C ทำหน้าที่เป็นคลูก (Child Class) อีกตัวหนึ่ง ที่เฉพาะเจาะจงว่าเป็นหนังเรื่อง "Titanic"
    # ถึงจะเป็นคนละเรื่องกับ B แต่ก็ "Inherit" ข้อมาจากแหล่งเดียวกันคือ Service A
    data = get_movie_info(6)
    return {
        "fetched_by": "Service C (Titanic)",
        "inheritance_info": "I am specifically 'Titanic', but my data comes from Service A",
        "inheritance_description": "Service C สืบทอดข้อมูลมาจาก Service A (Class A)",
        "movie_data": data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
