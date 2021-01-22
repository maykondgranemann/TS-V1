from dao.base_dao import BaseDao
from controller.base_controller import BaseController


def start_all_base_controller():
    instace = BaseController(BaseDao)

    assert isinstance(
        instace, BaseController), '[In Model]Instância base.controller não é do tipo especificado'
