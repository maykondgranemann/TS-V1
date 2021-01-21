import sys
sys.path.append('')
from controller.base_controller import BaseController
from controller.seller_controller import SellerController

class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)


#Testes#
if SellerController == BaseController:
    try:
        print('Ok')
    except Exception as e:
        assert isinstance(e, ValueError)