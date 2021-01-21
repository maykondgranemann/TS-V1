import sys
sys.path.append('.')

from back.tests.controllers.test_base_controller import start_base_controller_tests
from back.tests.controllers.test_seller_controller import start_seller_controller_tests
from back.tests.dao.test_base_dao import start_base_dao_tests
from back.tests.dao.test_seller_dao import start_test_seller_dao
from back.tests.models.test_base_model import start_test_base_model
from back.tests.models.test_seller_model import start_test_seller_model

def start_tests():
    try:
        print('\nIniciando testes... ')
        start_base_controller_tests()
        start_seller_controller_tests()
        start_base_dao_tests()
        start_test_seller_dao()
        start_test_base_model()
        start_test_seller_model()
        print('\nTestes conluídos com êxito')
    except Exception as e:
        raise Exception