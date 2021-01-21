import sys
sys.path.append('.')

from model.model_seller import Seller

# Testando inserção de atributos da model_seller
def test_should_save():

    name = "B2W"
    email = "contato@seller.com"
    phone = "(11)9 9999-9999"

    seller1 = Seller(name, email, phone)

    dao = Seller()
    dao.save(seller1)

    # Testando objeto da classe Seller
    assert isinstance(seller1, Seller)
