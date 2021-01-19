import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Seller(Base):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=64), nullable=False)
    phone = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=50), nullable=False)

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f""" {self.id} {self.name} {self.phone} {self.email} """