from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy import func

metadata = MetaData()


class Base(DeclarativeBase):
    metadata = metadata


class User(Base):

    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())