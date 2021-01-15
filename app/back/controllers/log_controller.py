from app.back.dao.log_dao import LogDao
from app.back.models.log import Log
from datetime import datetime

class LogController():
    def __init__(self):
        self.__dao = LogDao()

    def create(self, message) -> None:
        date = datetime.now()
        date = date.strftime('%d/%m/%Y - %H:%M:%S')
        log = Log(date, message)
        self.__dao.create(log)


    def read_all(self) -> list:
        return self.__dao.read_all()

# def create_log(message) -> None:
#     date = datetime.now()
#     date = date.strftime('%d/%m/%Y - %H:%M:%S')

#     log = Log(date, message)

#     set_log(log)
    
# def read_logs() -> list:
#     return get_log()
