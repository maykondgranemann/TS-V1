from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()  

class Seller(Base): 
    __tablename__ = 'seller'

    id = Column( Integer, primary_key=True )
    name = Column( String(length=100) )
    telephone = Column( String(length=20) )
    email = Column( String(length=50) )

    def __init__(self, name:str, telephone:str, email: str, id: str = None) -> None:
        self.name = name
        self.telephone = telephone
        self.email = email
        self.id = id