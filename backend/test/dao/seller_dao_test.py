from backend.models.seller_model import Seller
from backend.dao.seller_dao import SellerDao


def test_should_save():
    # given
    name = 'Adaa'
    email = 'a@a.comm'
    phone = '111-58585'
    seller = Seller(name, email, phone)

    # when
    dao = SellerDao()
    dao.save(seller)

    # then
    assert dao.read_all()[-1].name == name
    assert dao.read_all()[-1].email == email
    assert dao.read_all()[-1].phone == phone


def test_should_read_all():
    cont = SellerDao(Seller)
    seller = cont.read_all()

    assert isinstance((seller, list))


def test_should_read_by_id():
    pass


def test_should_update():
    pass


def test_should_delete():
    pass
