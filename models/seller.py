import sys
sys.path.append('.')

from sqlalchemy import Column, String
from models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'

    name = Column(String(length=100))
    email = Column(String(length=50))
    phone = Column(String(length=20))

    def __init__(self, name:str, email:str, phone:str, identifier:int = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.identifier = identifier

    def __str__(self):
        return f"Seller {self.name}, {self.email}, {self.phone}"
