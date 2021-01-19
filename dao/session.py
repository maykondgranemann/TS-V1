from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self) -> None:
        __connector = 'postgresql'
        __host = 'pgsql08-farm15.uni5.net'
        __user = 'topskills13'
        __password = 'olist123'
        __dbname = 'topskills13'
        self.__conn_string = f"{__connector}://{__user}:{__password}@{__host}:5432/{__dbname}"

    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)

        instace_session = sessionmaker(self.__engine)
        self.__session = instace_session()

        return self.__session

    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()
