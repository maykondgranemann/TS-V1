from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class Session:
    def __init__(self):
        host = getenv('DB_HOST')
        user = getenv('DB_USER')
        password = getenv('DB_PASSWORD')
        dbname = getenv('DB_NAME')
        port = getenv('DB_PORT', '5432')
        self.__conn_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

    def get_engine(self):
        return create_engine(self.__conn_string)

    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        S = sessionmaker(self.__engine)
        self.__session = S()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
        self.__engine.dispose()
