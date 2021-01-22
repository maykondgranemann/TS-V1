from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    identifier = Column(Integer, primary_key = True)