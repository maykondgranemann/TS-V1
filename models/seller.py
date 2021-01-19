from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Seller(Base):
    __tablename__ = 'seller'
    id = Column(Integer, primary_key=True)
    name = Column('nome', String(length=200))
    phone = Column('telefone', String(length=13))
    email = Column('email', String(length=200))

    def __init__(self, name: str, email: str, phone: str, id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
