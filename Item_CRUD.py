from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

# 아이템을 저장할 딕셔너리
items = {
    1: {"name": "아이템 1", "description": None, "price": 1000.0, "tax": 0.1},
    2: {"name": "아이템 2", "description": None, "price": 2000.0, "tax": 0.2},
    3: {"name": "아이템 3", "description": None, "price": 3000.0, "tax": 0.3},
}

# 아이템 조회 엔드포인트
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id in items:
        return {"item_id": item_id, "item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

# 아이템 생성 엔드포인트
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이템 ID입니다.")
    items[item_id] = item.dict()
    return {"message": f"아이템 {item_id}이(가) 생성되었습니다.", "item": items[item_id]}

# 아이템 삭제 엔드포인트
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": f"아이템 {item_id}이(가) 삭제되었습니다."}
    else:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다.")

# 애플리케이션 실행 코드 추가
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
