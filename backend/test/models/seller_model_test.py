from backend.dao.base_dao import BaseDao
from backend.dao.seller_dao import Seller


class TestSellerModel:

    name= 'sis'
    email = 's@s.com'
    phone = '99-999999'

    def test_should_it(self):
        seller = Seller(self.name, self.email, self.phone)
        assert seller.name is self.name
        assert seller.email is self.email
        assert seller.phone is self.phone


def start_test_model():
    test = TestSellerModel()
    test.test_should_it()