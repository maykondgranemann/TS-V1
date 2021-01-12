from app.back.dao.connection import get_connection


def set_log(message: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO log (message) VALUES ('{message}');")
    conn.commit()
    cursor.close()
    conn.close()

def get_log() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT message FROM log;')
    logs = cursor.fetchall()
    cursor.close()
    conn.close()
    return logs
