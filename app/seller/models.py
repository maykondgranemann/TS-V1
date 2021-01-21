from sqlalchemy import Column, String

from app.database.models import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    def __init__(self, fullname: str, email: str, phone: str) -> None:
        self.fullname = fullname
        self.email = email
        self.phone = phone