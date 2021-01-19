from sqlalchemy import Column, String
from .base_model import BaseModel


class Seller(BaseModel): 
    __tablename__ = 'sellers'

    name = Column( String(length=200) )
    email = Column( String(length=200) )
    phone = Column( String(length=200) )
    

    def __init__(self, name:str, email:str, phone: str, id: int = None):
        self.name = name
        self.email = email
        self.phone = phone

