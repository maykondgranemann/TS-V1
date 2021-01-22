from sqlalchemy import Column, String
from ATV_Ana.back.models.base_model import BaseModel
import re


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column('name', String(length=200))
    phone = Column('phone', String(length=200))
    email = Column('email', String(length=200))

    def __init__(self, name: str, phone: str, email: str) -> None:
        if validate_name(name):
            self.name = name
        if validate_phone(phone):
            self.phone = phone
        if validate_email(email):
            self.email = email


def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        raise ValueError("Email em formato incorreto")


def validate_name(name):
    if re.search('[a-zA-Z]', name):
        return True
    else:
        raise ValueError("Nome não pode possuir numeros")


def validate_phone(phone):
    if not re.search('[a-zA-Z]', phone):
        return True
    else:
        raise ValueError("Telefone não pode possuir letras")
