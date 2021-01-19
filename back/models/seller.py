from sqlalchemy import Column, String
from .base_model import BaseModel

class Seller(BaseModel): 
    __tablename__ = 'sellers'

    name = Column( String(length=200) )
    phone = Column( String(length=20) )
    email = Column( String(length=50) )

    def __init__(self, name:str, phone:str, email:str, id: int = None):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.id} {self.name} {self.phone} {self.email}"