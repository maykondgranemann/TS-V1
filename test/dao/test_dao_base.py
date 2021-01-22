import sys
sys.path.append('.')

from dao.dao_base import DaoBase
from model.model_seller import Seller
from dao.session import Session

# Testando inserção em dao_base
class TestBaseDao:

    name = 'Minha Mãe Só Por Deus!!!'
    email = 'contatodivino@sopordeus.com'
    phone = '(21) 9 6666-6666'
    id = None

    dao = DaoBase(Seller)

    def test_should_save(self):

        seller = Seller(self.name, self.email, self.phone)
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
            test = session.query(Seller).filter_by(name = self.name).first()
        seller = self.dao.read_by_id(id = self.id)

        self.dao.delete(seller)
        seller_deleted = self.dao.read_by_id(id = self.id)

        assert seller_deleted == None

def start_daobase_test():
    TestBaseDao().test_should_save()
    TestBaseDao().test_should_read_all()
    TestBaseDao().test_should_read_by_id()
    TestBaseDao().test_should_delete()

start_daobase_test()

# dao = DaoBase(Seller)
# result = dao.read_all()
# for s in  result:
#     print(s.name, s.id)
    