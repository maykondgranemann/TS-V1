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
    
def test_delete(): 
    base = BaseController(_dao)
    seller = Seller('Rafaela', '4199862-8989', 'rafa@teste.com')
    
    base.save(seller)
    r = base.read_all()[-1]
    s = base.read_by_id(r.id)
    assert base.delete(s) == None
    
    
def test_update(): 
    base = BaseController(_dao)
    seller = Seller('Rafaela', '4199862-8989', 'rafa@teste.com')
    
    base.save(seller)
    result = base.read_all()[-1]
    r = base.read_by_id(result.id)
    name = 'Teixeira Rafaela'
    email = '419987678997'
    phone = 'rafa@rafaela.com'
    r.name = name
    r.phone = phone
    r.email = email
    id = r.id
    
    base.save(r)
    s = base.read_by_id(id)
    
    assert name == s.name
    assert email == s.email
    assert phone == s.phone    
    
#test_read_all()    
#test_create()
#test_delete()
#test_update()
