from app.back.dao_txt.log_dao_txt import set_log, get_logs


def create_log(message: str) -> None:
    set_log(message)
    

def read_logs() -> list:
    return get_logs()