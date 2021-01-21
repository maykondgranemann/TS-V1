from app.database.dao import BaseDao
from app.seller.models import Seller


def test_base_dao_instance():
    class Test:
        pass

    dao = BaseDao(Test)

    assert isinstance(dao, BaseDao)
    assert dao._BaseDao__model_type is Test


def test_read_all_should_fetch_from_db():
    dao = BaseDao(Seller)

    result = dao.read_all()

    assert isinstance(result, list)


def test_save_should_save_to_db():
    dao = BaseDao(Seller)
    s = Seller('Testname', 'test@test.com', '9999999999')

    dao.save(s)
    result = dao.read_all()[-1]

    assert s.fullname == result.fullname
    assert s.email == result.email
    assert s.phone == result.phone

