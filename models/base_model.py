from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class BaseModel(Base):
    id = Column(Integer, primary_key=True)
