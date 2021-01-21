import sys
sys.path.append('.')
from backend.controllers.seller import SellerController
from backend.models.seller import Seller

a = SellerController()
# seller = Seller('Teste21', '9440' , 'marcello.santana@olist.com')
# a.save(seller)
result = a.read_by_id(92)
print(result.id, result.name, result.phone, result.mail)