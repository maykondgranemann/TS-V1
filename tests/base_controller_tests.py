class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def save(self, model: object) -> None:
        return self.__dao.create(model)

    def read_by_id(self, id: int) -> object:
        return self.__dao.read_by_id(id)

    def read_all(self, id: int) -> list:
        return self.__dao.read_all()

    def delete(self, id: int) -> object:
        self.__dao.delete(id)


#Testes#
if BaseController.save == None:
    try:
        print('ok')
    except Exception as error:
        assert isinstance(error, TypeError)

if BaseController.read_by_id is id(int):
    try:
        print('ok')
    except Exception as e:
        assert isinstance(error, TypeError)

if BaseController.read_all == id(int) and list:
    try:
        print('ok')
    except Exception as e:
        assert isinstance(error, TypeError)

if BaseController.delete == id(float) or object:
    try:
        print('id tem que ser int')
    except Exception as e:
        assert isinstance(e, TypeError)
