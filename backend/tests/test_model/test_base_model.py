from backend.models.base_model import BaseModel


class TestBaseModel:
    def test_base_model(self):
        model = BaseModel()
        assert model.__abstract__
        assert isinstance(model, BaseModel)
