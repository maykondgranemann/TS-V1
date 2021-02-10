from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    fullname = Column('fullname', String, nullable=False)
    phone = Column('phone', String, nullable=False)
    email = Column('email', String, nullable=False)

    def __init__(self, fullname: str, phone: str, email: str):
        self.fullname = fullname
        self.phone = phone
        self.email = email

    @validates('fullname')
    def validate_name(self, key: str, name: str):
        if not isinstance(name, str):
            raise TypeError(f"{key.capitalize()} must be a string")
        if not name.strip():
            raise ValueError(f"{key.capitalize()} must not be empty")
        if len(name) > 100:
            raise ValueError(f"{key.capitalize()} must be smaller than\
                                 50 characters")
        return name

    @validates('phone')
    def validate_phone(self, key: str, phone: str):
        if not isinstance(phone, str):
            raise TypeError(f"{key.capitalize()} must be a string")
        if not phone.strip():
            raise ValueError(f"{key.capitalize()} must not be empty")
        if 8 > len(phone) > 20:
            raise ValueError(f"{key.capitalize()} siz must be between 8 and\
                                 20 characters")
        return phone

    @validates('email')
    def validate_email(self, key: str, email: str):
        if not isinstance(email, str):
            raise TypeError(f"{key.capitalize()} must be a string")
        if not email.strip():
            raise ValueError(f"{key.capitalize()} must not be empty")
        if '@' not in email:
            raise ValueError(f"{key.capitalize()} must have a @ in it")
        return email

