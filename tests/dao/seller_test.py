from model.seller_model import Seller
from dao.seller_dao import SellerDao

name_ = 'Eletro do João'
phone_ = '41-9999-8888'
email_ = 'eletro@eletro.com'


def start_all_dao():
    create_instace()
    create_obj()
    test_method_create()()


def create_obj():
    obj = Seller(name_, phone_, email_)
    return obj


def create_instace():
    dao = SellerDao()
    assert isinstance(dao, SellerDao), 'Instância não é do tipo especificado'
    return dao


def test_method_create():
    dao = create_instace()
    obj = create_obj()
    result = dao.save(obj)
    obj_by_id = dao.read_all()[-1]

    assert result == None, 'O resultado de dao.save não foi o esperado'
    assert isinstance(
        obj_by_id, Seller), 'O objeto de retorno de dao.read_by_id não é o esperado'
    assert obj_by_id.name == name_, 'O resultado de obj.name não é satisfatório'
    assert obj_by_id.phone == phone_, 'O resultado de obj.phone não é satisfatório'
    assert obj_by_id.email == email_, 'O resultado de obj.email não é satisfatório'
    test_method_update(obj_by_id)


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
    obj_update = dao.read_by_id(id_temp)

    assert result == None, 'O resultado de dao.save não foi o esperado'
    assert isinstance(
        obj_update, Seller), 'O objeto de retorno de dao.read_by_id não é o esperado'
    assert obj_update.name == name2, 'O resultado de obj_update.name não é satisfatório'
    assert obj_update.phone == phone2, 'O resultado de obj_update.phone não é satisfatório'
    assert obj_update.email == email2, 'O resultado de obj_update.email não é satisfatório'
