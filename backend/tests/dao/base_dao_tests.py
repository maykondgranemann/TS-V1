import sys
sys.path.append('.')

from backend.models.seller import Seller
from backend.dao.base_dao import BaseDao


def test_read_all():
    result = BaseDao(Seller).read_all()
    
    assert isinstance(result, list)

def test_create():
    dao = BaseDao(Seller)
    name = 'Rafaela'
    email = '4199862-8989'
    phone = 'rafa@teste.com'
    seller = Seller(name, phone, email)
    
    dao.save(seller)
    r = dao.read_all()[-1]
    
    assert name == r.name
    assert email == r.email
    assert phone == r.phone
    
def test_delete(): 
    dao = BaseDao(Seller)
    seller = Seller('Rafaela', '4199862-8989', 'rafa@teste.com')
    
    dao.save(seller)
    r = dao.read_all()[-1]
    s = dao.read_by_id(r.id)
    assert dao.delete(s) == None
    
    
def test_update(): 
    dao = BaseDao(Seller)
    seller = Seller('Rafaela', '4199862-8989', 'rafa@teste.com')
    
    dao.save(seller)
    result = dao.read_all()[-1]
    r = dao.read_by_id(result.id)
    name = 'Teixeira Rafaela'
    email = '419987678997'
    phone = 'rafa@rafaela.com'
    r.name = name
    r.phone = phone
    r.email = email
    id = r.id
    
    dao.save(r)
    s = dao.read_by_id(id)
    
    assert name == s.name
    assert email == s.email
    assert phone == s.phone
    
    
    
#test_read_all()
#test_create()   
#test_delete()
#test_update()
