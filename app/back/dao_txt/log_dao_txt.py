from pathlib import Path
from datetime import datetime


_file = 'app/back/dao_txt/data/logs.txt'

def set_log(message: str) -> None:
    date = datetime.now()
    date = date.strftime('%d/%m/%Y - %H:%M:%S')
    file_path = Path(_file)
    if file_path.is_file():
        file = open(_file, "a")
    else:
        file = open(_file, "x")
    file.write(f'{date};{message}\n')
    

def get_logs() -> list:
    logs_list = []
    path = Path(_file)
    if path.is_file():
        file = open(_file, 'r')
        for line in file:
            logs_list.append(line.strip().split(';'))
        file.close()
    return logs_list