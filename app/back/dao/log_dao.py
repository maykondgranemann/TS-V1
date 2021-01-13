import psycopg2
from app.back.dao.connection import set_database, connection_credentials
from app.back.models.log import Log


def set_log(log: Log) -> None:
    date_message = f'{log.date};{log.message}'
    
    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO log (message) VALUES ('{date_message}');")
            conn.commit()
    except:
        print('An unexpected error has occurred')
        

def get_log() -> list:
    log_list = []

    try:
        set_database()
        with psycopg2.connect(connection_credentials()) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT message, id FROM log;')
            logs = cursor.fetchall()

            for log in logs:
                treated_log = str(log[0]).split(';')
                log = Log(treated_log[0], treated_log[1], log[1])
                log_list.append(log)
    except:
        print('An unexpected error has occurred')

    return log_list
