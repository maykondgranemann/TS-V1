import sys
sys.path.append('.')

from back.dao.seller_dao import SellerDao
from back.models.seller import Seller
from back.controllers.base_controller import BaseController
from back.dao.session import Session


class TestBaseController:
    selle_dao = SellerDao()
    base_controller = BaseController(selle_dao)
    object_name = "@2//*-#__12"
    object_phone = '789'
    object_email = 'teste@teste.com'
    
    def test_save(self):
        seller = Seller(self.object_name, self.object_phone, self.object_email)
        self.base_controller.save(seller)
        with Session() as session:
            model = session.query(Seller).filter_by(name=self.object_name).first()
        object_db_name = model.name
        assert object_db_name == self.object_name
        self.base_controller.delete(model)
        
    def test_delete(self):
        seller = Seller(self.object_name, self.object_phone, self.object_email)
        self.base_controller.save(seller)
        with Session() as session:
            model = session.query(Seller).filter_by(name=self.object_name).first()
        self.base_controller.delete(model)
        with Session() as session:
            model_after_delete = session.query(Seller).filter_by(name=self.object_name).first()
        assert model_after_delete is None

    def test_read_all(self):
        result = self.base_controller.read_all()
        assert isinstance(result, list)
        
    
    def test_read_by_id(self):
        model = self.base_controller.read_by_id(4)
        assert isinstance(model, Seller)


def start_base_controller_tests() -> None:
    test_base_controller = TestBaseController()
    test_base_controller.test_save()
    test_base_controller.test_delete()
    test_base_controller.test_read_all()
    test_base_controller.test_read_by_id()
