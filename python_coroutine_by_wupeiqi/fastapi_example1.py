import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    """普通操作接口"""
    # 某个 IO 操作 10s
    return {"message", "Hello world"}


if __name__ == '__main__':
    uvicorn.run("fastapi_example1:app", host="127.0.0.1", port=5000, log_level="info")
