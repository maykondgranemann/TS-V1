from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#criacao de classe para conexão com DC
class Session:
    def __init__(self) -> None:
        conector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills2'
        password = 'olist21'
        dbname = 'topskills2'
        self.__conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"

#criacao de classe para incialização do BD
    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

#criacao de classe para fechamento do BD
    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()