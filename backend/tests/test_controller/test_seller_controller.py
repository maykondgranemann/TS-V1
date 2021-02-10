from backend.controllers.base_controller import BaseController
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller
from dotenv import load_dotenv
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest
from sqlalchemy.exc import DataError, ProgrammingError


class FakeSeller:
    fullname = 'josué fake'
    email = 'fake@email.com'
    phone = 'fake123'


class TestSellerController:
    @pytest.fixture
    def setup(self):
        load_dotenv()
        self.controller = SellerController()
        self.name = 'Josué Ávila'
        self.email = 'josue.avila@olist.com'
        self.phone = '41997879889'
        self.seller = Seller(self.name, self.phone, self.email)

    def test_controller_isinstance(self, setup):
        assert isinstance(self.controller, SellerController)
        assert isinstance(self.controller, BaseController)

    def test_read_all_method(self, setup):
        sellers = self.controller.read_all()
        assert isinstance(sellers, list)
        assert all(isinstance(item, Seller) for item in sellers)

    def test_read_by_id_method(self, setup):
        sample_product = self.controller.read_all()[0]
        read_by_id_product = self.controller.read_by_id(sample_product.id)
        assert sample_product.id == read_by_id_product.id
        assert isinstance(read_by_id_product, Seller)
        try:
            result_test = self.controller.read_by_id('string')
        except Exception as e:
            assert isinstance(e, DataError)

        try:
            fake = FakeSeller()

            result_test = self.controller.read_by_id(fake)
        except Exception as e:
            assert isinstance(e, ProgrammingError)

        try:
            test_list = [1, 2, 3]
            result_test = self.controller.read_by_id(test_list)
        except Exception as e:
            assert isinstance(e, ProgrammingError)

    def test_save_method(self, setup):
        result = self.controller.save(self.seller)
        identifier = result[0]
        state_persistent = result[1]
        saved_seller = self.controller.read_by_id(identifier)
        assert isinstance(saved_seller, Seller)
        assert isinstance(identifier, int)
        assert saved_seller.fullname == self.name
        assert saved_seller.phone == self.phone
        assert saved_seller.email == self.email
        assert state_persistent

        try:
            value_test = 'string'
            self.controller.save(value_test)
        except Exception as e:
            assert isinstance(e, UnmappedInstanceError)

        fake = FakeSeller()
        try:
            self.controller.save(fake)
        except Exception as e:
            assert isinstance(e, UnmappedInstanceError)

    def test_save_method_exceptions(self, setup):
        try:
            value_test = 'string'
            self.controller.save(value_test)
        except Exception as e:
            assert isinstance(e, UnmappedInstanceError)

        fake = FakeSeller()
        try:
            self.controller.save(fake)
        except Exception as e:
            assert isinstance(e, UnmappedInstanceError)

    def test_update_method(self, setup):
        result = self.controller.save(self.seller)
        identifier = result[0]
        saved_seller = self.controller.read_by_id(identifier)

        new_name = 'Josué Rosa de Ávila'
        new_email = 'josue.rosadeavila@gmail.com'
        new_phone = '42999437330'

        saved_seller.fullname = new_name
        saved_seller.email = new_email
        saved_seller.phone = new_phone

        result = self.controller.save(saved_seller)
        same_identifier = result[0]
        state_updated = result[1]
        updated_seller = self.controller.read_by_id(same_identifier)

        assert isinstance(updated_seller, Seller)
        assert updated_seller.fullname == new_name
        assert updated_seller.phone == new_phone
        assert updated_seller.email == new_email
        assert state_updated
        self.controller.delete(updated_seller)

    def test_delete_method(self, setup):
        id_ = self.controller.save(self.seller)[0]
        seller_to_delete = self.controller.read_by_id(id_)
        state_deleted = self.controller.delete(seller_to_delete)
        assert state_deleted

        try:
            value_test = 'string'
            self.controller.delete(value_test)
        except Exception as e:
            assert isinstance(e, UnmappedInstanceError)

        fake = FakeSeller()
        try:
            self.controller.delete(fake)
        except Exception as e:
            assert isinstance(e, UnmappedInstanceError)
