from app.back.dao.base_dao import BaseDao
from app.back.models.log import Log

class LogDao(BaseDao):
    def create(self, log: Log):
        date_message = f'{log.date};{log.message}'
        query = f"INSERT INTO log (message) VALUES ('{date_message}');"
        super().execute(query)


    def read_all(self) -> list:
        query = f"SELECT message, id FROM log;"
        result_list = super().read(query)
        logs = []
        for result in result_list:
            treated_log = str(result[0]).split(';')
            log = Log(treated_log[0], treated_log[1], result[1])
            logs.append(log)
        return logs
