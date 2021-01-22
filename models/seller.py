from sqlalchemy import Column, String

from models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    name = Column('nome', String(length=200))
    phone = Column('telefone', String(length=13))
    email = Column('email', String(length=200))

    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
