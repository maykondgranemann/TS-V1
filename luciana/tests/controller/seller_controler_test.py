import sys
sys.path.append('.')

from luciana.controller.controller_seller import SellerController
from luciana.controller.controller_base import BaseController

if SellerController == BaseController:
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, ValueError)
