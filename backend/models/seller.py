from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    __fullname = Column('fullname', String)
    __phone = Column('phone', String)
    __email = Column('email', String)

    def __init__(self, fullname: str, phone: str, email: str):
        self.fullname = fullname
        self.phone = phone
        self.email = email

    @property
    def fullname(self) -> str:
        return self.__fullname

    @fullname.setter
    def fullname(self, value: str) -> None:
        self.__fullname = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        self.__phone = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        if isinstance(value, str):
            self.__email = value
        else:
            raise ValueError
