import asyncio

import aioredis
import uvicorn
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()

# 创建 redis 连接池
REDIS_POOL = aioredis.ConnectionsPool('redis://127.0.0.1:6379', password='test', minsize=1, maxsize=10)


@app.get("/")
def index():
    """普通操作接口"""
    # 某个 IO 操作 10s
    return {"message", "Hello world"}


@app.get('/red')
async def red():
    """异步操作接口"""

    print("请求来了")

    await asyncio.sleep(3)

    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)

    # 设置值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    REDIS_POOL.release(conn)

    return result


if __name__ == '__main__':
    uvicorn.run("fastapi_example2:app", host="127.0.0.1", port=5000, log_level="info")
