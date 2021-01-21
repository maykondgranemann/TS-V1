from sqlalchemy import Column, String, Integer
from back.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column(String)
    phone = Column(String)
    mail = Column(String)

    def __init__(self, name:str, phone:str, mail:str) -> None:
        self._name = name
        self._phone = phone
        self._mail = mail

    @property
    def _name(self) -> str:
        return self.name

    @property
    def _phone(self) -> str:
        return self.phone

    @property
    def _mail(self) -> str:
        return self.mail

    @_name.setter
    def _name(self, name) -> None:
        if isinstance(name, str):
            self.name = str(name)
        else:
            raise TypeError("Name must be a string")
    
    @_phone.setter
    def _phone(self, phone) -> None:
        if isinstance(phone, str):
            self.phone = str(phone)
        else:
            raise TypeError("Phone must be a string")

    @_mail.setter
    def _mail(self, mail) -> None:
        if isinstance(mail, str):
            self.mail = str(mail)
        else:
            raise TypeError("Mail must be a string")
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Phone: {self.phone}, Mail: {self.mail}"
