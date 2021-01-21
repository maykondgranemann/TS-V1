from sqlalchemy import Column, String

from .base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column(String(length=100))
    phone = Column(String(length=22))
    email = Column(String(length=100))

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Seller Name: {self.name} - Seller id: {self.id}'
