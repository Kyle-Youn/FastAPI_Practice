from fastapi import FastAPI

app = FastAPI

@app.get("/")
acync def get_root():
  return {"message": "Hello Wolrd!"}
