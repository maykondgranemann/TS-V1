import sys
sys.path.append('')
from luciana.dao.base_dao import BaseDao
from luciana.dao.session import Session
from luciana.models.base_model import BaseModel

#Testes#
if BaseDao.save == BaseModel:
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseDao.read_all == (list):
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseDao.read_by_id == id(int):
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseDao.delete == BaseModel:
    try:
        print('pass')
    except Exception as error:
        assert isinstance(error, TypeError)