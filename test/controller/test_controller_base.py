import sys
sys.path.append('.')

from controller.controller_base import BaseController


# Testando inserção de dados via Controller_base
def test_should_save():

    name = 'Americanas'
    email = 'contato@americanas.com'
    phone = '11 999999999'

    seller2 = BaseController(name, email, phone)

    dao = BaseController()
    dao.save(seller2)

    assert isinstance(seller2, BaseController)
