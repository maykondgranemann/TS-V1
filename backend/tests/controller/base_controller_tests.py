import sys
sys.path.append('.')

from backend.controller.base_controller import BaseController
from backend.dao.seller_dao import SellerDao
from backend.models.seller import Seller

_dao = SellerDao()

def test_read_all():
    result = BaseController(_dao).read_all()
    
    assert isinstance(result, list)

def test_create():
    base = BaseController(_dao)
    name = 'Rafaela Teixeira'
    phone = 'rafa@teste.com'
    email = '4199862-8989'
    seller = Seller(name, phone, email)
    
    base.save(seller)
    r = base.read_all()[-1]
    
    assert name == r.name
    assert phone == r.phone
    assert email == r.email
    
#test_read_all()    
#test_create()
