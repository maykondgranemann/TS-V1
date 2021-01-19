from backend.models.base_model import BaseModel
import sqlalchemy as db


class Seller(BaseModel):
    __tablename__ = 'seller'
    name = db.Column(db.String(length=50))
    phone = db.Column(db.String(length=50))
    mail = db.Column(db.String(length=50))

    def __init__(self, name: str, phone: str, mail: str):
        self.name = name
        self.phone = phone
        self.mail = mail
