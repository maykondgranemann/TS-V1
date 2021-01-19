from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self) -> None:
        bd = 'postgresql'
        host='pgsql08-farm15.uni5.net'
        user='topskills7'
        password='olist21'
        database='topskills7'
        self.__connection_string = f"{bd}://{user}:{password}@{host}:5432/{database}"
        
    def __enter__(self):
        self.__engine = create_engine(self.__connection_string)        
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session
    
    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()
        