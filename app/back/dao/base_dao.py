from app.back.dao.connection import Connection

class BaseDao:
    def execute(self, query: str) -> None:
        try:
            with Connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
        except Exception as error:
            print(error)
    
    def read(self, query: str) -> list:
        try:
            with Connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
            return result
        except Exception as error:
            print(error)
