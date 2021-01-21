import sys
sys.path.append('')
from controller.base_controller import BaseController
from controller.seller_controller import SellerController

#Testes#
if SellerController == BaseController:
    try:
        print('Ok')
    except Exception as error:
        assert isinstance(error, ValueError)