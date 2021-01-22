import sys
sys.path.append('.')

from controller.controller_base import BaseController
from model.model_seller import Seller
from dao.session import Session


# Testando inserção de dados via Controller_base
class TestBaseController:

    name = 'Só Por Deus!!!'
    email = 'contato@sopordeus!!!.com'
    phone = '(11) 9 6666-6666'
    id = None

    dao = BaseController(Seller)

    def test_should_save(self):

        seller = BaseController(self.name, self.email, self.phone)
        self.dao.save(seller)
        with Session() as session:
            test = session.query(Seller).filter_by(name = self.name).first()

        assert self.name == test
        self.id = test

    def test_should_read_all(self):
        seller = self.dao.read_all()

        assert isinstance(seller, list)

    def test_should_read_by_id(self):
        with Session() as session:
            test = session.query(Seller).filter_by(id = self.id).first()
        seller = self.dao.read_by_id(id = test)

        assert isinstance(seller, Seller)

    def test_should_delete(self):
        with Session() as session:
            test = session.query(Seller).filter_by(id = self.id).first()
        seller = self.dao.read_by_id(id = self.id)

        self.dao.delete(seller)
        seller_deleted = self.dao.read_by_id(id = self.id)

        assert seller_deleted == None

def start_controllerbase_test():

    TestBaseController().test_should_save()
    TestBaseController().test_should_read_all()
    TestBaseController().test_should_read_by_id()
    TestBaseController().test_should_delete()

start_controllerbase_test()
