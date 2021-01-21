from sqlalchemy import Column, Integer, String
from ..models.base_model import BaseModel

class Seller(BaseModel): 
    __tablename__ = 'sellers'

    name = Column( String(length=100) )
    phone = Column( String(length=20) )
    email = Column( String(length=50) )

    def __init__(self, name:str, phone:str, email: str, id: str = None) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id