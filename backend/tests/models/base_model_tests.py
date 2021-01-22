import sys
sys.path.append('.')

from backend.models.base_model import BaseModel


def test_base_model():
    base = BaseModel()

    assert isinstance(base, BaseModel)
    
#test_base_model()    

