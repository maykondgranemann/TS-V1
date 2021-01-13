from app.back.dao.connection import get_connection
from app.back.models.log import Log


def set_log(log: Log) -> None:
    date_message = f'{log.date};{log.message}'

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO log (message) VALUES ('{date_message}');")
        conn.commit()


def get_log() -> list:
    log_list = []

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT message, id FROM log;')
        logs = cursor.fetchall()

        for log in logs:
            treated_log = str(log[0]).split(';')
            log = Log(treated_log[0], treated_log[1], log[1])
            log_list.append(log)

        return log_list
