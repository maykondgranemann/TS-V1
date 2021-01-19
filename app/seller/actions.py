from typing import List

from app.seller.dao import SellerDao
from app.seller.exceptions import SellerNotFoundException
from app.seller.models import Seller

DAO = SellerDao()


def create(fullname: str, email: str, phone: str) -> None:
    model = Seller(fullname, email, phone)
    DAO.save(model)


def read_all() -> List[Seller]:
    return DAO.read_all()


def read_by_id(id: int) -> Seller:
    try:
        result = DAO.read_by_id(id)
    except SellerNotFoundException:
        raise Exception('Seller not found.')
    return result


def update(fullname: str, email: str, phone: str, id: int) -> None:
    model = read_by_id(id)
    model.fullname = fullname
    model.email = email
    model.phone = phone
    DAO.save(model)


def delete(id: int) -> None:
    model = read_by_id(id)
    DAO.delete(model)
