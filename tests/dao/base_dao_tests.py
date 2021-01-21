import sys
sys.path.append('')
from dao.base_dao import BaseDao
from model.base_model import BaseModel
from dao.session import Session

#Testes#
if BaseDao.save == BaseModel:
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseDao.read_all == (list):
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseDao.read_by_id == id(int):
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseDao.delete == BaseModel:
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)
