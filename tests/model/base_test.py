from model.base_model import BaseModel

id_ = 10


def start_all_base_model():
    instance = BaseModel()
    instance.id = id_

    assert isinstance(
        instance, BaseModel), '[In Model]Instância base.model não é do tipo especificado'
    assert type(instance.id) == int, '[In Model] O tipo de instance.id não é o esperado'
