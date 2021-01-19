from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Seller(Base):
    __tablename__ = 'seller'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    email = Column(String(length=50))
    phone = Column(String(length=15))
    
    def __init__(self, name:str, email:str, phone:str) -> None:
        self.name = name
        self.email = email
        self.phone = phone

