from sqlalchemy import Column, String

class Seller():
    __tablename__ = 'seller'

    name = Column(String(length=200))
    phone = Column(String(length=20))
    email = Column(String(length=200))


    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email
