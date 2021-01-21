from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self)-> None:
        database = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills13'
        password = 'olist123'
        dbname = 'topskills13'
        self.__conn_string = f"{database}://{user}:{password}@{host}:5432/{dbname}"

    def __enter__(self)-> object:
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, traceback)-> None:
        self.__session.close()
        self.__engine.dispose()
