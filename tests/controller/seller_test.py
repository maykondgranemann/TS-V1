from model.seller_model import Seller
from controller.seller_controller import SellerController

name_ = 'Maria e João'
phone_ = '41-9999-7777'
email_ = 'mj@mariaejoao.com'


def start_all_controller():
    create_obj()
    create_instace()
    test_method_create()


def create_obj():
    obj = Seller(name_, phone_, email_)
    assert isinstance(
        obj, Seller), '[In Controller]Objeto não é do tipo esperado'
    return obj


def create_instace():
    control = SellerController()
    assert isinstance(
        control, SellerController), '[In Controller]Instância não é do tipo esperado'
    return control


def test_method_create():
    control = create_instace()
    obj = create_obj()
    result = control.save(obj)
    assert result == None, '[In Control]O resultado de control.save não foi o esperado'

    list_messy = control.read_all()
    assert isinstance(
        list_messy, list), '[In Control]A lista de retorno de control.read_all não é do tipo esperado'

    list_ordered = sorted(list_messy, key=lambda k: k.id)
    obj = list_ordered[-1]

    assert isinstance(
        obj, Seller), '[In Control]O objeto de retorno de control.read_all não é o esperado'
    assert obj.name == name_, '[In Control]O resultado de obj.name não é satisfatório'
    assert obj.phone == phone_, '[In Control]O resultado de obj.phone não é satisfatório'
    assert obj.email == email_, '[In Control]O resultado de obj.email não é satisfatório'
    test_method_update(obj)


def test_method_update(obj: Seller):
    control = create_instace()
    id_temp = obj.id

    name2 = 'Smartphones do José'
    phone2 = '45 999-4848'
    email2 = 'contato@josesmart.com'

    obj.name = name2
    obj.phone = phone2
    obj.email = email2
    result = control.save(obj)
    assert result == None, '[In control]O resultado de control.save não foi o esperado'

    obj_update = control.read_by_id(id_temp)
    assert isinstance(
        obj_update, Seller), '[In control]O objeto de retorno de control.read_by_id não é o esperado'
    assert obj_update.name == name2, '[In control]O resultado de obj_update.name não é satisfatório'
    assert obj_update.phone == phone2, '[In control]O resultado de obj_update.phone não é satisfatório'
    assert obj_update.email == email2, '[In control]O resultado de obj_update.email não é satisfatório'
    test_method_delete(obj_update)


def test_method_delete(obj: Seller):
    control = create_instace()
    id_temp = obj.id
    obj_delete = control.read_by_id(id_temp)
    result = control.delete(obj_delete)
    assert result == None, '[In control]O resultado de control.delete não foi o esperado'
