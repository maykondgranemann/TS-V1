from ATV_Ana.back.models.base_model import BaseModel
from ATV_Ana.back.dao.session import Session


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def create_update(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            sellers = session.query(self.__type_model).all()
        return sellers

    def read_by_id(self, id_: int):
        with Session() as session:
            sel = session.query(self.__type_model).filter_by(id=id_).first()
        return sel

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()


#testes

#create_update(Seller("Ana Paula", "12132312", "ana@teste.com"))

# for i in read_all():
#    print(i.name, i.phone, i.email, i.id)

# seller = read_by_id(21)
# print(seller.name, seller.id, seller.email)

#seller.name = "novo seller"
#seller.email = "new@seller.com"

#create_update(seller)

#delete(seller)
