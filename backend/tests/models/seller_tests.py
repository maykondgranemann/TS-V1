import sys
sys.path.append('.')

from backend.models.seller import Seller


def test_seller_model():
    name = 'Rafaela'
    email = '4199862-8989'
    phone = 'rafa@teste.com'
    seller = Seller(name, email, phone)

    assert isinstance(seller, Seller)
    assert isinstance(seller.name, str)
    assert isinstance(seller.email, str)
    assert isinstance(seller.phone, str)
    assert seller.__tablename__ == 'seller'
    assert seller.name == name
    assert seller.email == email
    assert seller.phone == phone

#test_seller_model()





