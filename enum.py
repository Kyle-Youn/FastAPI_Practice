from enum import Enum
from fastapi import FastAPI

class Color(str, Enum):
  red = "red"
  green = "green"
  blue = "blue"

app = FastAPI()

@app.get("/colors/{color_name}")
async def get_color(color_name: Color):
  return {"color": color_name}
