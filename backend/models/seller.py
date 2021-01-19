from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SellerModel(Base):
    __tablename__ = 'seller'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    phone = Column(String)
    email = Column(String)

    def __init__(self, fullname: str, phone: str, email: str, id: int = None):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.email = email
