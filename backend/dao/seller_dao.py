from backend.dao.session import Session
from backend.models.seller import Seller

class SellerDao:
    def save(self, obj: Seller) -> None:
        with Session() as s:
            s.add(obj)
            s.commit()
            
    def read_all(self) -> list:
        with Session() as s:
            result = s.query(Seller).all()   
        return result
    
    def read_by_id(self, id:int):
        with Session() as s:
            result = s.query(Seller).filter_by(id=id).first()
        return result 
    
    def delete(self, obj:Seller) -> None:
        with Session() as s:
            s.delete(obj)
            s.commit()  