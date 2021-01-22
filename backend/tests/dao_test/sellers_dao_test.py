import sys
sys.path.append('.')

from backend.dao.sellers_dao import SellerDao
from backend.models.sellers import Seller

#test read all type
obj=SellerDao()
assert isinstance(obj.read_all_dao(),list)

#test read by id type
assert isinstance(obj.read_by_id_dao(2),Seller)

#test save
obj_aux=Seller("teste 22/01","4444333222211","@@@@@@@@@@@",445)
obj.save_dao(obj_aux)
assert isinstance(obj.read_by_id_dao(444),Seller)

#test delete
obj_aux=obj.read_by_id_dao(679)
id=obj_aux.id
obj.delete_dao(obj_aux)
assert obj.read_by_id_dao(id)==None

#test register bd
obj_aux=obj.read_by_id_dao(2)
assert obj_aux.name=='gustavo sobreiro'
assert obj_aux.email=='gustavo.sobreiro@olist.com'
assert obj_aux.phone=='34232341423'
