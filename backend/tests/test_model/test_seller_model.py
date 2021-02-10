import pytest
from backend.models.base_model import BaseModel
from backend.models.seller import Seller


class TestSellerModel:
    @pytest.fixture
    def setup(self):
        self.name = 'Josué Ávila'
        self.email = 'josue.avila@olist.com'
        self.phone = '41997879889'
        self.seller = Seller(self.name, self.phone, self.email)
        return self.seller

    def test_seller_isinstance(self, setup):
        assert isinstance(self.seller, Seller)
        assert isinstance(self.seller, BaseModel)

    def test_gets_and_sets_name(self, setup):
        assert self.seller.fullname == self.name
        assert type(self.name) == type(self.seller.fullname)
        assert isinstance(self.seller.fullname, str)
        assert self.seller.fullname is self.name

    def test_gets_and_sets_email(self, setup):
        assert self.seller.email == self.email
        assert type(self.email) == type(self.seller.email)
        assert isinstance(self.seller.email, str)
        assert self.seller.email is self.email

    def test_gets_and_sets_phone(self, setup):
        assert self.seller.phone == self.phone
        assert type(self.phone) == type(self.seller.phone)
        assert isinstance(self.seller.email, str)
        assert self.seller.phone is self.phone

    def test_model_exceptions(self, setup):
        try:
            new_test_name = None
            self.seller.fullname = new_test_name
        except Exception as e:
            assert isinstance(e, TypeError)

        try:
            new_test_email = None
            self.seller.email = new_test_email
        except Exception as e:
            assert isinstance(e, ValueError)

        try:
            new_test_phone = None
            self.seller.phone = new_test_phone
        except Exception as e:
            assert isinstance(e, TypeError)

        try:
            new_test_email = 1
            self.seller.email = new_test_email
        except Exception as e:
            assert isinstance(e, ValueError)
