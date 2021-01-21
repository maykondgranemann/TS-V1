from sqlalchemy import Column, String
from model.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column(String(length=200))
    phone = Column(String(length=200))
    email = Column(String(length=200))


    def __init__(self, name: str, phone: str, email: str, id: int=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id

    def __str__(self):
        return f"{self.id} {self.name} {self.phone} {self.email}"