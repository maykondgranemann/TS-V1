from app.back.dao.log_dao import set_log, get_log


def create_log(message: str) -> None:
    set_log(message)
    
def read_logs() -> list:
    return get_log()
