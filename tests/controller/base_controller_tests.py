import sys
sys.path.append('')
from controller.base_controller import BaseController

#Testes#
if BaseController.save == None:
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseController.read_by_id is id(int):
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseController.read_all == id(int) and list:
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseController.delete == id(float) or object:
    try:
        print('id tem que ser int')
    except Exception as error:
        assert isinstance(error, TypeError)
