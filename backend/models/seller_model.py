from backend.models.base_model import BaseModel
from sqlalchemy import Column, String


class Seller(BaseModel):
    __tablename__ = 'sellers'
    name = Column(String(length=64), nullable=False)
    phone = Column(String(length=50), nullable=False)
    email = Column(String(length=50), nullable=False)

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f""" {self.id} {self.name} {self.phone} {self.email} """
