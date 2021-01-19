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
