from fastapi import FastAPI, HTTPException

app = FastAPI()

# 샘플 데이터
items = {
    1: {"name": "아이템 1"},
    2: {"name": "아이템 2"},
    3: {"name": "아이템 3"},
}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": f"아이템 {item_id}이(가) 성공적으로 삭제되었습니다."}
    else:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
