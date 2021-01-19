from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Session:
    def __init__(self):
        connector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills5'
        password = 'olist123'
        dbname = 'topskills5'
        self.__conn_string = f'{connector}://{user}:{password}@{host}:5432/{dbname}'
        
    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__session.dispose()