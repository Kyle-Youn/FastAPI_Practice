from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# 데이터베이스 연결 함수
def get_db_connection():
    return psycopg2.connect(
        dbname="your_database",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
    )

# 데이터베이스 연결 테스트
@app.on_event("startup")
async def startup_event():
    try:
        conn = get_db_connection()
        conn.close()
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        exit(1)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
