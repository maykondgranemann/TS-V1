import sys
sys.path.append('.')

from sqlalchemy import Column, String
from backend.models.base_model import *


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column(String(length=(100)))
    email = Column(String(length=(30)))
    phone = Column(String(length=(18)))

    def __init__(self, name: str, phone: str, email: str, id: int=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id

    def __str__(self):
        return f'ID: {self.id}///Nome: {self.name}////Telefone: {self.phone}///Email: {self.email}'