import sys
sys.path.append('.')
from backend.models.seller import Seller


name_test = 'User_teste'

phone_test = '81129440'

mail_test = 'teste@olist.com'

seller_test = Seller(name_test,phone_test, mail_test)

#Teste de Classe 
assert isinstance(seller_test, Seller)

#Teste de setter e getters name
assert seller_test.name is name_test
#Testando valores não string em name
new_test_name = 10
try:
    seller_test.set_name(new_test_name)
except Exception as e:
    assert isinstance(e , ValueError) 

#Testando setter e getters phone
assert seller_test.phone is phone_test
#Testando valores não String em Phone
new_phone_test = 10
try:
    seller_test.set_phone(new_phone_test)
except Exception as e:
    assert isinstance(e, ValueError)

#Testando setter e getters mail
assert seller_test.mail is mail_test
#Testando valores não string em Mail
new_mail_test = 'mail'
try:
    seller_test.set_mail(new_mail_test)
except Exception as e:
    assert isinstance(e, ValueError)
