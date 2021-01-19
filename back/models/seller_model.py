import sys
sys.path.append('.')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

from back.dao.connection import Connection

Base = declarative_base()

class Seller(Base):
    __tablename__ = 'seller'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    mail = Column(String)

    def __init__(self, name:str, phone:str, mail:str) -> None:
        self.name = name
        self.phone = phone
        self.mail = mail

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Phone: {self.phone}, Mail: {self.mail}"