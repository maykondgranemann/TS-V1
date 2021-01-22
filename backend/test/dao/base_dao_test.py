from backend.dao.base_dao import BaseDao
from backend.models.seller_model import Seller
from backend.dao.session import Session


class TestBaseDao:
    name = 'Idi'
    email = 'i@i.com'
    phone = '33-3333333'
    id = None

    dao = BaseDao(Seller)

    def test_should_save(self):
        seller = Seller(self.name, self.email, self.phone)
        self.dao.save(seller)
        with Session() as session:
            object_test = session.query(Seller).filter_by(name=self.name).first()
        assert self.name == object_test.name
        self.id = object_test.id

    def test_should_read_all(self):
        sellers = self.dao.read_all()
        assert isinstance(sellers, list)

    def test_should_read_by_id(self):
        with Session() as session:
            object_test = session.query(Seller).filter_by(name=self.name).first()
        seller = self.dao.read_by_id(id=object_test.id)

        assert isinstance(seller, Seller)

    def test_should_delete(self):
        with Session() as session:
            object_test = session.query(Seller).filter_by(name=self.name).first()
        seller = self.dao.read_by_id(id=object_test.id)

        self.dao.delete(seller)
        seller_after_deleted = self.dao.read_by_id(id=self.id)
        assert seller_after_deleted is None


def start_basedao_test():
    TestBaseDao().test_should_save()
    TestBaseDao().test_should_read_all()
    TestBaseDao().test_should_read_by_id()
    TestBaseDao().test_should_delete()


start_basedao_test()
