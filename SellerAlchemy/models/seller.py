import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Seller(Base):
    __tablename__ = 'sellers'

    id = sql.Column( sql.Integer, primary_key=True )
    name = sql.Column( sql.String(length=200), nullable=False )
    phone = sql.Column( sql.String(length=11), nullable=False )
    email = sql.Column( sql.String(length=200), nullable=False )

    def __init__(self, name: str, phone: str, email: str, id: int = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
