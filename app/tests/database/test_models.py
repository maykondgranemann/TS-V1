from app.database.models import BaseModel


def test_base_model_instance():
    model = BaseModel()

    assert isinstance(model, BaseModel)
    assert model.__abstract__
    assert hasattr(model, 'id')
    assert hasattr(model, 'created_at')
    assert hasattr(model, 'updated_at')
