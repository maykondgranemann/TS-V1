import sys
sys.path.append('.')

from back.models.seller import Seller


class TestSellerModel:
    
    seller_name = 'Seller Name'
    seller_phone = '41-99999999'
    seller_email = 'seller@mail.com'
    
    def test_atributes(self):
        seller = Seller(self.seller_name, self.seller_phone, self.seller_email)
        assert isinstance(seller, Seller)
        assert seller.name is self.seller_name
        assert seller.phone is self.seller_phone
        assert seller.email is self.seller_email

def start_test_seller_model():
    test_seller_model = TestSellerModel()
    test_seller_model.test_atributes()
