import sqlalchemy as db
from models.base_model import BaseModel


class Seller(BaseModel):
    __tablename__ = 'sellers'

    name = db.Column(db.String(length=200))
    phone = db.Column(db.String(length=11))
    email = db.Column(db.String(length=200))

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.id} - {self.name} - {self.phone} - {self.email}'
