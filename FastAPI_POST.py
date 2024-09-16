'''
pip install fastapi
pip install uvicorn
'''


from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# 임시 데이터 저장소
items = {
    1: {"name": "Item 1", "price": 100},
    2: {"name": "Item 2", "price": 200},
    3: {"name": "Item 3", "price": 300}

# 특정 아이템을 삭제하는 DELETE 요청 처리
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": f"Item {item_id} deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
