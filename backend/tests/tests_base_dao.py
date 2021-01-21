import sys
sys.path.append('.')
from backend.dao.base_dao import BaseDao
from backend.models.seller import Seller

dao_teste = BaseDao(Seller)

#Testando save passando um argumento que não sej filho de BaseModel
try:
    dao_teste.save('')
except Exception as e:
    assert isinstance(e, ValueError)

#testando Delete passando um argumento que não seja filgo de BaseModel
try:
    dao_teste.delete('')
except Exception as e:
    assert isinstance(e, ValueError)

#Testando retornos das funções de listagem
assert isinstance(dao_teste.read_all(), list)
assert isinstance(dao_teste.read_by_id(92), Seller)
#teste caso não haja retorno para a query desejada
assert dao_teste.read_by_id(500) is None