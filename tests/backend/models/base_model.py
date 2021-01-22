from backend.models.base_model import BaseModel


base_model = BaseModel()

assert isinstance(base_model, BaseModel)
assert base_model.__abstract__
assert hasattr(base_model, 'id')