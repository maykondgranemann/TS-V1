from sqlalchemy import Column, String, Integer
from back.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column(String)
    phone = Column(String)
    mail = Column(String)

    def __init__(self, name:str, phone:str, mail:str) -> None:
        self.name = name
        self.phone = phone
        self.mail = mail

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Phone: {self.phone}, Mail: {self.mail}"