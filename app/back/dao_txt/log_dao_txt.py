from pathlib import Path
from datetime import datetime


_file_name = 'app/back/dao_txt/data/logs.txt'

def set_log(message: str) -> None:
    date = datetime.now()
    date = date.strftime('%d/%m/%Y - %H:%M:%S')

    with open(_file_name, 'a') as file:
            file.write(f'{date};{message}\n')

   

def get_logs() -> list:
    logs_list = []
    with open(_file_name, 'a') as file:
        for line in file:
            logs_list.append(line.strip().split(';'))
       
    return logs_list