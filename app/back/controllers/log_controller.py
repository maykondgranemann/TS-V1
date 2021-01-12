from app.back.dao.log_dao import set_log, get_log
from app.back.models.log import Log
from datetime import datetime

def create_log(message) -> None:
    date = datetime.now()
    date = date.strftime('%d/%m/%Y - %H:%M:%S')

    log = Log(date, message)

    set_log(log)
    
def read_logs() -> list:
    return get_log()
