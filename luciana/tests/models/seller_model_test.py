import sys
sys.path.append('.')

from sqlalchemy import Column, String
from luciana.models.seller import Seller

#Testes#
name = 'a'
try:
    Seller.name = name 
except Exception as error:
    assert isinstance(e, ValueError)

phone = '11223344556'
try:
    Seller.phone = phone 
except Exception as error:
    assert isinstance(e, ValueError)

email = 'quesia@carrefour.com'
try:
    Seller.email = email 
except Exception as error:
    assert isinstance(e, ValueError)