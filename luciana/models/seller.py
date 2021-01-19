import sys
sys.path.append('.')

from sqlalchemy import Column, String
from luciana.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'

    nome = Column(String(length = 80))
    email = Column(String(length = 50))
    telefone = Column(String(length = 15))

    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def __str__(self):
        return f'Seller Name: {self.nome} - Seller id: {self.id}'
    