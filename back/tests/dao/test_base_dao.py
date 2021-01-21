import sys
sys.path.append('.')

from back.dao.base_dao import BaseDao
from back.models.seller import Seller
from back.dao.seller_dao import SellerDao
from back.dao.session import Session


class TestBaseDao:
    base_dao = BaseDao(Seller)
    object_name = "!@#$%¨$*&//"
    object_phone = '123'
    object_email = 'ze@ze.com'
    
    
    def test_instantiate_a_class(self) -> None:
         assert isinstance(self.base_dao , BaseDao)
         
    def test_save(self) -> None:
        s = Seller(self.object_name, self.object_phone, self.object_email)
        self.base_dao.save(s)
        with Session() as session:
            model = session.query(Seller).filter_by(name=self.object_name).first()
        object_db_name = model.name
        assert object_db_name == self.object_name
        self.base_dao.delete(model)
              
    def test_delete(self) -> None:
        s = Seller(self.object_name, self.object_phone, self.object_email)
        self.base_dao.save(s)
        with Session() as session:
            model = session.query(Seller).filter_by(name= self.object_name).first()
        self.base_dao.delete(model)
        with Session() as session:
            model_after_delete = session.query(Seller).filter_by(name=self.object_name).first()
        assert model_after_delete is None
    
    def test_save_string(self) -> None:
        try:
            BaseDao.save('string')
        except Exception as e:
            assert isinstance(e, TypeError)        
    
    def test_save_integer(self) -> None:
        try:
            BaseDao.save(1)
        except Exception as e:
            assert isinstance(e, TypeError) 
    
    def test_read_all(self) -> None:
        result = self.base_dao.read_all()
        if len(result) > 0:
            assert isinstance(result, list)
        else:
            print("Database is empty")
    
    def test_read_by_id_using_an_integer_id(self) -> None:
        result = self.base_dao.read_by_id(4)
        assert isinstance(result, Seller)

    def test_read_by_id_using_an_string_id(self) -> None:
        try:
            result = self.base_dao.read_by_id('string')
        except Exception as e:
            assert isinstance(e, NameError)  

    def test_delete_using_an_string(self) -> None:
        try:
            self.base_dao.delete('string')
        except Exception as e:
            assert isinstance(e, NameError) 
    
    def test_delete_using_an_integer(self) -> None:
        try:
            self.base_dao.delete(1)
        except Exception as e:
            assert isinstance(e, NameError)      


def start_base_dao_tests():
    test_base_dao = TestBaseDao()
    test_base_dao.test_instantiate_a_class()
    test_base_dao.test_save()
    test_base_dao.test_delete()
    test_base_dao.test_save_string()
    test_base_dao.test_save_integer()
    test_base_dao.test_read_all()
    test_base_dao.test_read_by_id_using_an_integer_id()
    test_base_dao.test_read_by_id_using_an_string_id()
    test_base_dao.test_delete_using_an_string()
    test_base_dao.test_delete_using_an_integer()
  