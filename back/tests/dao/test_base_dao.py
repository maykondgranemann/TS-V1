import sys
sys.path.append('.')

from back.dao.base_dao import BaseDao
from back.models.seller import Seller
from back.dao.seller_dao import SellerDao

class TestBaseDao:
    
    def test_instantiate_a_class(self):
         test_object = BaseDao(Seller)
         assert isinstance(test_object, BaseDao)
      
    def test_save_string(self):
        try:
            BaseDao.save('string')
        except Exception as e:
            assert isinstance(e, TypeError)        
    
    def test_save_integer(self):
        try:
            BaseDao.save(1)
        except Exception as e:
            assert isinstance(e, TypeError) 
    
    def test_read_all(self):
        seller_test = BaseDao(Seller)
        result = seller_test.read_all()
        if len(result) > 0:
            assert isinstance(result, list)
        else:
            print("Database is empty")
    
    def test_read_by_id_using_an_integer_id(self):
        seller_test = BaseDao(Seller)
        result = seller_test.read_by_id(4)
        assert isinstance(result, Seller)

    def test_read_by_id_using_an_string_id(self):
        seller_test = BaseDao(Seller)
        try:
            result = seller_test.read_by_id('string')
        except Exception as e:
            assert isinstance(e, NameError)  

    def test_delete_using_an_string(self):
        seller_test = BaseDao(Seller)
        try:
            seller_test.delete('string')
        except Exception as e:
            assert isinstance(e, NameError) 
    
    def test_delete_using_an_integer(self):
        seller_test = BaseDao(Seller)
        try:
            seller_test.delete(1)
        except Exception as e:
            assert isinstance(e, NameError)           
