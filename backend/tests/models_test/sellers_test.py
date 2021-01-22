import sys
sys.path.append('.')

from backend.models.sellers import Seller


seller_aux = Seller('MAcarena maria', '000001111', 'macarena@f.com')

#test type
assert isinstance(seller_aux.name,str)
assert isinstance(seller_aux.phone,str)
assert isinstance(seller_aux.email,str)

#test value
assert seller_aux.name=='MAcarena maria'
assert seller_aux.phone=='000001111'
assert seller_aux.email=='macarena@f.com'