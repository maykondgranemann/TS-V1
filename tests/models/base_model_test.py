import sys

sys.path.append('.')

from models.base_model import BaseModel


id = 1;
base_model = BaseModel(id)
#assert base_model.id == id