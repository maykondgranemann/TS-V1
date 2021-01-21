from sqlalchemy import Column, String 
#que nem no base_model.
from luciana.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'

    nome = Column(String(length = 100))
    email = Column(String(length = 50))
    telefone = Column(String(length = 20))

# Função __init__ com as propriedades definidas
    def __init__(self, nome: str, email: str, telefone: str, id: int = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def __str__(self):
        return f'Seller Name: {self.nome}'
    