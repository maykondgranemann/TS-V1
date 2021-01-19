import sys
sys.path.append('/teste/')

from dao.session import Session

class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model
    
    def save(self, model) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result
    
    def read_by_id(self, identifier: int):
        with Session() as session:
            result = session.query(self.__type_model).filter_by(id = identifier).first()
        return result

    def delete(self, model) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()