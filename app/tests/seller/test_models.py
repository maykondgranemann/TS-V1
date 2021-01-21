from app.database.models import BaseModel
from app.seller.models import Seller


def test_seller_model_instance():
    fullname = 'fullname'
    email = 'mail@test.com'
    phone = '99999999999'

    model = Seller(fullname, email, phone)

    assert isinstance(model, BaseModel)
    assert isinstance(model, Seller)
    assert model.__tablename__ == 'seller'
    assert model.fullname == fullname
    assert model.email == email
    assert model.phone == phone
