import sys
sys.path.append('.')

from luciana.controller.controller_base import BaseController

if BaseController.save == None:
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, ValueError)

if BaseController.read_all == id(int) and list:
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, ValueError)

if BaseController.read_by_id is id(int):
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, ValueError)

if BaseController.delete == id(float) or object:
    try:
        print('Must be an int')
    except Exception as error:
        assert isinstance(error, ValueError)