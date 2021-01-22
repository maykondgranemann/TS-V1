from model.seller_model import Seller

name_ = 'Eletro eletro'
phone_ = '41-9999-8888'
email_ = 'eletro@eletro.com'


def start_all_model():
    test_obj_seller()
    test_return_seller()


def instace_object():
    obj_seller = Seller(name_, phone_, email_)
    return obj_seller


def test_obj_seller():
    obj = instace_object()
    assert isinstance(obj, Seller), '[In Model]Objeto não é do tipo especificado'


def test_return_seller():
    obj = instace_object()
    assert isinstance(
        obj.name, str), '[In Model]O retorno para "name" não é do tipo esperado'
    assert isinstance(
        obj.phone, str), '[In Model]O retorno "phone" não é do tipo esperado'
    assert isinstance(
        obj.email, str), '[In Model]O retorno "email" não é do tipo esperado'

    assert obj.name == name_, '[In Model]A saída de "name" não é válida ou igual a entrada'
    assert obj.email == email_, '[In Model]A saída de "email" não é válida ou igual a entrada'
    assert obj.phone == phone_, '[In Model]A saída de "phone" não é válida ou igual a entrada'
