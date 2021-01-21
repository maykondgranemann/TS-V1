import sys
sys.path.append('.')
from backend.dao.seller import SellerDao
from backend.models.seller import Seller

#validação caso a classe passada não seja filha de BaseModel
try:
    seller = SellerDao()
except Exception as e:
    assert isinstance(e, ValueError)