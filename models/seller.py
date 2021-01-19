from sqlalchemy import Column, String

from .base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'sellers'

    name = Column(String(length=100))
    phone = Column(String(length=22))
    email = Column(String(length=100))

    def __str__(self):
        return f'Seller id: {self.id} - Seller Name: {self.name}'
