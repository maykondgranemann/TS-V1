from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import String
from model.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'sellers'
    __name = Column('name', String(length=50))
    __phone = Column('phone', String(length=50))
    __email = Column('email', String(length=50))

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self) -> str:
        return self.__name

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def email(self) -> str:
        return self.__email

    @name.setter
    def name(self, name):
        self.__name = name

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email
