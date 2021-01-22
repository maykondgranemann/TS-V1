import sys
sys.path.append('.')

from backend.controller.sellers_controller import SellerController
from backend.models.sellers import Seller


seller_tst=SellerController()
#test of type return 
assert isinstance( seller_tst.read_all_ctrl(),list)
assert isinstance( seller_tst.read_by_id_ctrl(6),Seller)


nome='joao'
num='4444'
email='ewwww@ffff.com'
obj=Seller(nome,num,email)
#test type and value
assert isinstance(obj.name,str)
assert obj.name==nome
#test type and value
assert isinstance(obj.phone,str)
assert obj.phone==num
#test type and value
assert isinstance(obj.email,str)
assert obj.email==email
#test read by id
obj2=SellerController().read_by_id_ctrl(2).email
assert obj2=='gustavo.sobreiro@olist.com'
#test update
obj3=SellerController().read_by_id_ctrl(6)
obj3.phone='98854-8900'
SellerController().save_ctrl(obj3)
obj3=SellerController().read_by_id_ctrl(6)
assert obj3.phone=='98854-8900'
#test delete
obj4=SellerController().read_by_id_ctrl(88)
id=obj4.id
SellerController().delete_ctrl(obj4)
obj4=SellerController().read_by_id_ctrl(id)
assert obj4==None



