import sys
sys.path.append('')
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


#Testes#
name = 'Quésia'
try:
    Seller.name = name 
except Exception as e:
    assert isinstance(e, ValueError)

phone = '(28) 99999-9999'
try:
    Seller.phone = phone 
except Exception as e:
    assert isinstance(e, ValueError)

email = 'quesia@carrefour.com'
try:
    Seller.email = email 
except Exception as e:
    assert isinstance(e, ValueError)