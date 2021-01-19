from sqlalchemy import Column, VARCHAR
from models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'seller'

    name = Column( VARCHAR(length=100) )
    telephone = Column( VARCHAR(length=20) )
    email = Column( VARCHAR(length=50) )

    def __init__(self, name: str, telephone: str, email: str) -> None:
        self.name = name
        self.telephone = telephone
        self.email = email
