from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model):
        conector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills6'
        dbname = 'topskills6'
        password = 'olist123'
        conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"
        engine = create_engine(conn_string)
        Session = sessionmaker(engine)
        self.__session = Session()
        self.__type_model = type_model

    def save(self, model: BaseModel) -> None:
        self.__session.add(model)
        self.__session.commit()

    def read_all(self) -> list:
        result = self.__session.query(self.__type_model).all()
        return result

    def read_by_id(self, id: int) -> BaseModel:
        model = self.__session.query(self.__type_model).filter_by(id=id).first()
        return model

    def delete(self, model: BaseModel) -> None:
        self.__session.delete(model)
        self.__session.commit()