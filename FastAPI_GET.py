'''
pip install fastapi
pip install uvicorn
'''


from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# 루트 경로에 대한 GET 요청 처리
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
