from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "q": "test"}