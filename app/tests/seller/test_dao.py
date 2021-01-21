from app.database.dao import BaseDao
from app.seller.dao import SellerDao
from app.seller.models import Seller


def test_seller_dao_instance():
    dao = SellerDao()

    assert isinstance(dao, SellerDao)
    assert isinstance(dao, BaseDao)
    assert dao._BaseDao__model_type is Seller
