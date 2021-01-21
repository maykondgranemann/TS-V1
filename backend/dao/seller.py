from backend.dao.base_dao import BaseDao
from backend.models.seller import Seller
from backend.models.base_model import BaseModel

class SellerDao(BaseDao):
    def __init__(self):
        if isinstance(Seller, BaseModel):
            super().__init__(Seller)
        else:
            raise ValueError('This Class must be to receive a BaseModel Object')
