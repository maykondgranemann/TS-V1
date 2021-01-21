import sys
sys.path.append('')
from sqlalchemy import Column, String
from model.seller_model import Seller

#Testes#
name = 'Quésia'
try:
    Seller.name = name 
except Exception as error:
    assert isinstance(e, ValueError)

phone = '(28) 99999-9999'
try:
    Seller.phone = phone 
except Exception as error:
    assert isinstance(e, ValueError)

email = 'quesia@carrefour.com'
try:
    Seller.email = email 
except Exception as error:
    assert isinstance(e, ValueError)