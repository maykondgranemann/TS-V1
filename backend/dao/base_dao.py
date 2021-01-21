from backend.dao.session import Session
from backend.models.base_model import BaseModel

class BaseDao:
    def __init__(self, type_model: str = None) -> None:
        self.__type_model = type_model
    
    def save(self, obj: BaseModel) -> None:
        with Session() as s:
            s.add(obj)
            s.commit()
            
    def read_all(self) -> list:
        with Session() as s:
            result = s.query(self.__type_model).all()   
        return result
    
    def read_by_id(self, id:int) -> BaseModel:
        with Session() as s:
            result = s.query(self.__type_model).filter_by(id=id).first()
        return result 
    
    def delete(self, obj: BaseModel) -> None:
        with Session() as s:
            s.delete(obj)
            s.commit()  