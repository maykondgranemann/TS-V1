from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __id = Column('id', Integer, primary_key=True)

    @property
    def id(self) -> int:
        return self.__id
