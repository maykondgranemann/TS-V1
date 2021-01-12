from datetime import datetime
from app.back.dao.connection import get_connection


def set_log(message: str) -> None:
    date = datetime.now()
    date = date.strftime('%d/%m/%Y - %H:%M:%S')
    date_message = f'{date};{message}'

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO log (message) VALUES ('{date_message}');")
    conn.commit()
    cursor.close()
    conn.close()

def get_log() -> list:
    log_list = []

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT message FROM log;')
    logs = cursor.fetchall()
    cursor.close()
    conn.close()

    for log in logs:
        treated_log = str(log).split(';')
        log_list.append(treated_log)

    return log_list
