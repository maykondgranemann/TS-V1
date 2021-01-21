import sys
sys.path.append('.')

from controllers.seller_controller import SellerController
from models.seller import Seller


#testando o insert
seller = Seller('Lucas Torres', '41997536991', 'lucas.torres@olist.com')
id = SellerController().save(seller)

seller = SellerController().read_by_id(id)
assert seller.name == 'Lucas Torres'
assert seller.telephone == '41997536991'
assert seller.email == 'lucas.torres@olist.com'


#Testando o read_all()
sellers = SellerController().read_all()
assert isinstance(sellers, list)