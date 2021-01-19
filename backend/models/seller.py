from sqlalchemy import Column, String
from backend.models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    fullname = Column(String)
    phone = Column(String)
    email = Column(String)

    def __init__(self, fullname: str, phone: str, email: str):
        self.fullname = fullname
        self.phone = phone
        self.email = email
