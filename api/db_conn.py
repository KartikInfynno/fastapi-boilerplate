from os import chdir
from os.path import abspath, join, dirname

from typing import Optional, AsyncIterable

from api.tables import Base
from api.config import config

from fastapi import Depends

from alembic import command
from alembic.config import Config

from sqlalchemy.engine import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

_db_connection: Optional[Engine]


def init_db():
    # create tables
    open_database_connection_pools()
    global _db_connection
    if not _db_connection:
        raise Exception("DB not connected.")
    Base.metadata.create_all(_db_connection)

    # then load the Alembic configuration and generate the
    # version table, "stamping" it with the most recent rev:
    path = abspath(join(dirname(__file__), ".."))
    chdir(path)
    alembic_cfg = Config("alembic.ini")
    command.stamp(alembic_cfg, "head")


def open_database_connection_pools():
    global _db_connection
    _db_connection = create_engine(url=str(config.database_url),
                                   pool_size=config.database_pool_size,
                                   echo=False,
                                   future=True)


def close_database_connection_pools():
    global _db_connection
    if _db_connection:
        _db_connection.dispose()


async def get_db_connection() -> Engine:
    global _db_connection
    if _db_connection is None:
        raise RuntimeError("Database connection is not initialized")
    return _db_connection


async def get_session(db_conn=Depends(get_db_connection)
                      ) -> AsyncIterable[Session]:
    session = Session(bind=db_conn)

    try:
        yield session
    finally:
        session.close()
