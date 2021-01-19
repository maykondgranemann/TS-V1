from sqlalchemy import Column, String, Integer
from back.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String)
    description = Column(String)
    price = Column(String)

    def __init__(self, name:str, description:str, price:str) -> None:
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"