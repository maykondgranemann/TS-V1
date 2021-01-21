import sys
sys.path.append('.')

from dao.dao_base import DaoBase

# Testando inserção em dao_base
def test_should_save():

    name = 'Amazon'
    email = 'contato@amazon.com'
    phone = '11 999999999'

    seller3 = DaoBase(name, email, phone)

    dao = DaoBase()
    dao.save(seller3)

    assert isinstance(seller3, DaoBase)
