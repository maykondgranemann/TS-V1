from ..model.model_base import BaseModel

# Criar classe base para a DAO 
class DaoBase:
    def save(self, model:BaseModel) -> None:
        self.__session.add(model)
        self.__session.commit()

    def read_all(self) -> list:
        return self.__session.query(BaseModel).all()

    def read_by_id(self, id_:int) -> BaseModel:
        return self.__session(BaseModel).filter_by(id=id).first()

    def delete(self, model: BaseModel) -> None:
        self.__session.delete(model)
        self.__session.commit()