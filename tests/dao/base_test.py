from model.seller_model import Seller
from dao.base_dao import BaseDao


def start_all_base_dao():
    instace = BaseDao(Seller)

    assert isinstance(
        instace, BaseDao), '[In Model]Instância base.dao não é do tipo especificado'
