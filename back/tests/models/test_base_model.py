import sys
sys.path.append('.')

from back.models.base_model import BaseModel


class TestBaseModel:
    
    def test_instance(self):
        test_base_model = BaseModel()
        assert isinstance (test_base_model, BaseModel)
