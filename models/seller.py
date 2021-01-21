from sqlalchemy import Column, String
from .base import BaseModel

class Seller(BaseModel):
    __tablename__ = 'sellers'

    name = Column( String(length = 200) )
    email = Column( String(length = 30) )
    phone = Column( String(length = 20) )

    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone