# Importar a BaseModel de model_base.py
from .model_base import BaseModel

# Importar do sqlalchemy Column e Integer assim como no model_base
from sqlalchemy import Column, String 

# Criar a classe Seller referenciando a tabela no BD via __tablename__
class Seller(BaseModel):
    __tablename__ = 'seller'

# Criar as colunas assim como estão no DB
    name = Column(String(length=(100)))
    email = Column(String(length=(30)))
    phone = Column(String(length=(18)))

# Criar uma função __init__ com as propriedades definidas
    def __init__(self, name: str, email: str, phone: str, id: int=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {self.id}"
