from sqlalchemy import Column, String
from ATV_Ana.back.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column(String(length=200))
    phone = Column(String(length=200))
    email = Column(String(length=200))

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
