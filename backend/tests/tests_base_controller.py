import sys
sys.path.append('.')
from backend.controllers.base_controller import BaseController
from backend.dao.seller import SellerDao
from backend.models.seller import Seller

base_test = BaseController(SellerDao())
seller_name = 'Marcello'
seller_phone = '81129440'
seller_mail = 'marcello.santana@olist.com'
seller_test = Seller(seller_name,seller_phone,seller_mail)
seller_test.id = 81
#base_test.save(seller_test)


#Testando retornos das funções da BaseController
assert isinstance(base_test.read_all(), list)
assert isinstance(base_test.read_by_id(55), Seller)

#Testando excessão da função save caso não seja uma classe herdada de Basemodel
try:
    base_test.save('')
except Exception as e:
    assert isinstance(e, ValueError)

#Testando a exceção da função delete caso não seja uma classe herdada de Basemodel
try:
    base_test.delete(8)
except Exception as e:
    assert isinstance(e, ValueError)
#Testando a execeção das funções de listagem caso não haja elementos seguindo a query
assert base_test.read_by_id(100) is None
# assert base_test.read_all() is None

# Testando passar uma dao que não herda de BaseDao
try:
    base_test = BaseController('a')
except Exception as e:
    assert isinstance(e, ValueError)
