from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import String
from model.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'sellers'
    name = Column(String(length=50))
    phone = Column(String(length=50))
    email = Column(String(length=50))

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
