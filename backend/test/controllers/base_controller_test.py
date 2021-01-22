from backend.controllers.base_controller import BaseController
from backend.models.seller_model import Seller
from backend.dao.seller_dao import SellerDao
from backend.dao.session import Session


class TestBaseController:
    seller_dao = SellerDao()
    base_controller = BaseController(seller_dao)
    name = 'odo'
    email = 'o@o.com'
    phone = '11-11111'
    id = None

    def test_should_save(self):
        seller = Seller(self.name, self.email, self.phone)
        self.controller.save(seller)
        with Session() as session:
            object_test = session.query(Seller).filter_by(name=self.name).first()
        assert self.name == object_test.name
        self.id = object_test.id

    def test_should_read_all(self):
        sellers = self.controller.read_all()
        assert isinstance(sellers, list)

    def test_should_read_by_id(self):
        with Session() as session:
            object_test = session.query(Seller).filter_by(name=self.name).first()
        seller = self.controller.read_by_id(id=object_test.id)

        assert isinstance(seller, Seller)

    def test_should_delete(self):
        with Session() as session:
            object_test = session.query(Seller).filter_by(name=self.name).first()
        seller = self.controller.read_by_id(id=object_test.id)

        self.controller.delete(seller)
        seller_after_deleted = self.controller.read_by_id(id=self.id)
        assert seller_after_deleted is None


def start_base_controller_test() -> None:
    TestBaseController().test_should_save()
    TestBaseController().test_should_read_all()
    TestBaseController().test_should_read_by_id()
    TestBaseController().test_should_delete()


start_base_controller_test()
