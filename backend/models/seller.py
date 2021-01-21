from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    
    __name = Column('name', String(length=100))
    __email = Column('email', String(length=50))
    __phone = Column('phone', String(length=15))
        
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
        
    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str) -> None:
        self.__phone = phone
