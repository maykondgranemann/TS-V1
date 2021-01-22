import sys
sys.path.append('.')

from backend.controller.base_controller import BaseController
from backend.dao.sellers_dao import SellerDao
from backend.models.sellers import Seller

access_BC = BaseController(SellerDao)

obj_seller=Seller('van daime','4333333','vanvan@gmail.com',2345)

#test save
access_BC.save_ctrl(obj_seller)
obj_aux=access_BC.read_by_id_ctrl(2345)
assert obj_aux.id==2345

#test type read all
assert isinstance(access_BC.read_all_ctrl(),list)

#test return read all
obj2_aux=access_BC.read_all_ctrl()
assert obj2_aux != None

#test  type read by id 
assert isinstance(access_BC.read_by_id_ctrl(2345),Seller)

#test return read by id
obj3_aux=access_BC.read_by_id_ctrl(2345)
assert obj3_aux !=None

#test delete
access_BC.delete_ctrl(obj3_aux)
obj4_aux=access_BC.read_by_id_ctrl(2345)
assert obj3_aux ==None