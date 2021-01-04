import pytz
from datetime import datetime


def get_datetime_str_sao_paulo() -> str:
    date = datetime.now(pytz.timezone("America/Sao_Paulo"))
    return f'{date.hour}:{date.minute}:{date.second} - {date.day}/{date.month}/{date.year}'


def write_to_logs(operation_name: str) -> None:
    with open(f'logs.txt', 'a') as file:
        file.write(f'\n{get_datetime_str_sao_paulo()} - {operation_name}')


def write_to_txt_store(data: str, file_name: str) -> None:
    with open(f'{file_name}.txt', 'a') as file:
        file.write(f'\n{data}')
