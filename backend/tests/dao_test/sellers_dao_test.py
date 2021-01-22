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
obj_aux=Seller("teste 22/01","4444333222211","@@@@@@@@@@@",700)
obj.save_dao(obj_aux)
assert isinstance(obj.read_by_id_dao(678),Seller)

#test delete
obj_aux=obj.read_by_id_dao(93)
id=obj_aux.id
obj.delete_dao(obj_aux)
assert obj.read_by_id_dao(id)==None

