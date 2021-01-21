import sys
sys.path.append('.')

from back.dao.base_dao import BaseDao
from back.models.seller import Seller
from back.dao.seller_dao import SellerDao
from back.dao.session import Session


class TestBaseDao:
    
    def test_instantiate_a_class(self) -> None:
         test_object = BaseDao(Seller)
         assert isinstance(test_object, BaseDao)
         
    def test_save(self) -> None:
        test = BaseDao(Seller)
        object_name = "!@#$%¨$*&//"
        object_phone = '123'
        object_email = 'ze@ze.com'
        s = Seller(object_name, object_phone, object_email)
        test.save(s)
        with Session() as session:
            model = session.query(Seller).filter_by(name='!@#$%¨$*&//').first()
        object_db_name = model.name
        assert object_db_name == object_name
        test.delete(model)
              
    def test_delete(self) -> None:
        test = BaseDao(Seller)
        object_name = "!@#$%¨$*&//"
        object_phone = '123'
        object_email = 'ze@ze.com'
        s = Seller(object_name, object_phone, object_email)
        test.save(s)
        with Session() as session:
            model = session.query(Seller).filter_by(name='!@#$%¨$*&//').first()
        test.delete(model)
        with Session() as session:
            model_after_delete = session.query(Seller).filter_by(name='!@#$%¨$*&//').first()
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
        seller_test = BaseDao(Seller)
        result = seller_test.read_all()
        if len(result) > 0:
            assert isinstance(result, list)
        else:
            print("Database is empty")
    
    def test_read_by_id_using_an_integer_id(self) -> None:
        seller_test = BaseDao(Seller)
        result = seller_test.read_by_id(4)
        assert isinstance(result, Seller)

    def test_read_by_id_using_an_string_id(self) -> None:
        seller_test = BaseDao(Seller)
        try:
            result = seller_test.read_by_id('string')
        except Exception as e:
            assert isinstance(e, NameError)  

    def test_delete_using_an_string(self) -> None:
        seller_test = BaseDao(Seller)
        try:
            seller_test.delete('string')
        except Exception as e:
            assert isinstance(e, NameError) 
    
    def test_delete_using_an_integer(self) -> None:
        seller_test = BaseDao(Seller)
        try:
            seller_test.delete(1)
        except Exception as e:
            assert isinstance(e, NameError)      
