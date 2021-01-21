from backend.controllers.base_controller import BaseController
from backend.dao.seller import SellerDao
from backend.dao.base_dao import BaseDao

class SellerController(BaseController):
    def __init__(self):
        dao = SellerDao()
        if isinstance(dao, BaseDao):
            super().__init__(dao)
        else:
            raise TypeError('Dao type is not Basedao')

