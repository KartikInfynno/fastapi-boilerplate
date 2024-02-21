from json import loads, dumps
from typing import Optional

import dotenv
from pydantic.networks import PostgresDsn, HttpUrl
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Config(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 80
    debug: bool = False
    trace: bool = False

    database_url: str
    database_pool_size: int = 50

    class Config:
        env_prefix = 'test_' ## Add your prefix here


config = Config()  # type: ignore
