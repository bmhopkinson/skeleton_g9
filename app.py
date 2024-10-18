from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 

class RequestModel(BaseModel):
    source: str
    message: str
    verion: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def echo(data: RequestModel):
    return dict(data)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)