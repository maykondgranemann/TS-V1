from app.seller.exceptions import SellerNotFoundException


def test_seller_not_found_exception_instance():
    exc = SellerNotFoundException()

    assert isinstance(exc, Exception)
    assert exc.args[0] == 'Seller not found!'
