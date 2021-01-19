from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def __init__(self):
        conector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills1'
        password = 'olist21'
        dbname = 'topskills1'
        self.__conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"

    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session
    
    def __exit__(self, type, value, traceback):
        self.__engine.dispose()
        self.__session.close()