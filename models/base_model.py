from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class BaseModel(Base):
    ___abtract__ = True
    id = Column(Integer, primary_key=True)
