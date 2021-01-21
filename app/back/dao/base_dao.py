from .session import Session
from ..models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model) -> None:
        self.type_model = type_model

    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def update(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.type_model).order_by('id').all()
        return result

    def read_by_id(self, id: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.type_model).filter_by(id=id).first()
        return result    
    
    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
