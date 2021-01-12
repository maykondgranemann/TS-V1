from app.back.dao.connection import get_connection
from app.back.models.log import Log


def set_log(log: Log) -> None:
    date_message = f'{log.date};{log.message}'

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
    cursor.execute(f'SELECT message, id FROM log;')
    logs = cursor.fetchall()
    cursor.close()
    conn.close()

    for log in logs:
        treated_log = str(log[0]).split(';')
        log = Log(treated_log[0], treated_log[1], log[1])
        print(log.date, log.message)
        log_list.append(log)

    return log_list
