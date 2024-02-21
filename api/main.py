import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

from api.db_conn import open_database_connection_pools, close_database_connection_pools
from api.config import config
from api.test_router.router import router as test_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    open_database_connection_pools()
    yield
    close_database_connection_pools()


app = FastAPI(lifespan=lifespan)


app.include_router(test_router)


@app.get("/")
def create_user():
    return {"details": "Hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host=config.host, port=config.port)
