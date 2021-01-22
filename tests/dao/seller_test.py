from model.seller_model import Seller
from dao.seller_dao import SellerDao

name_ = 'Eletro do João'
phone_ = '41-9999-8888'
email_ = 'eletro@eletro.com'


def start_all_dao():
    create_instace()
    create_obj()
    test_method_create()


def create_obj():
    obj = Seller(name_, phone_, email_)
    assert isinstance(obj, Seller), '[In Dao]Objeto não é do tipo esperado'
    return obj


def create_instace():
    dao = SellerDao()
    assert isinstance(
        dao, SellerDao), '[In Dao]Instância não é do tipo esperado'
    return dao


def test_method_create():
    dao = create_instace()
    obj = create_obj()
    result = dao.save(obj)
    assert result == None, '[In Dao]O resultado de dao.save não foi o esperado'

    list_messy = dao.read_all()
    assert isinstance(
        list_messy, list), '[In Dao]A lista de retorno de dao.read_all não é do tipo esperado'

    list_ordered = sorted(list_messy, key=lambda k: k.id)
    obj = list_ordered[-1]

    assert isinstance(
        obj, Seller), '[In Dao]O objeto de retorno de dao.read_all não é o esperado'
    assert obj.name == name_, '[In Dao]O resultado de obj.name não é satisfatório'
    assert obj.phone == phone_, '[In Dao]O resultado de obj.phone não é satisfatório'
    assert obj.email == email_, '[In Dao]O resultado de obj.email não é satisfatório'
    test_method_update(obj)


def test_method_update(obj: Seller):
    dao = create_instace()
    id_temp = obj.id

    name2 = 'Eletronicos'
    phone2 = '45 999-999'
    email2 = 'contato@eletronicos.com'

    obj.name = name2
    obj.phone = phone2
    obj.email = email2
    result = dao.save(obj)
    assert result == None, '[In Dao]O resultado de dao.save não foi o esperado'

    obj_update = dao.read_by_id(id_temp)
    assert isinstance(
        obj_update, Seller), '[In Dao]O objeto de retorno de dao.read_by_id não é o esperado'
    assert obj_update.name == name2, '[In Dao]O resultado de obj_update.name não é satisfatório'
    assert obj_update.phone == phone2, '[In Dao]O resultado de obj_update.phone não é satisfatório'
    assert obj_update.email == email2, '[In Dao]O resultado de obj_update.email não é satisfatório'
    test_method_delete(obj_update)


def test_method_delete(obj: Seller):
    control = create_instace()
    id_temp = obj.id
    obj_delete = control.read_by_id(id_temp)
    result = control.delete(obj_delete)
    assert result == None, '[In Dao]O resultado de dao.delete não foi o esperado'
