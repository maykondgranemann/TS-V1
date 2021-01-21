from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

#variável que recebe a função declarative_base()
Base = declarative_base()

#Este arquivo deve conter todas informações comuns
#a outras models, como é o caso do 'id'
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key = True)
