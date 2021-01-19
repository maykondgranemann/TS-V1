import sys
sys.path.append('.')

from sqlalchemy import Column, String
from models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'seller'

    name_seller = Column(String(length=100))
    email = Column(String(length=50))
    phone = Column(String(length=20))

    def __init__(self, name:str, email:str, phone:str):
        self.name_seller = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Seller {self.name_seller}, {self.email}, {self.phone}"
