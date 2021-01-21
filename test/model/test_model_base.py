from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
import sys 
sys.path.append('.')

from model.model_base import BaseModel


# Testando ID em model_base
assert type(id) == BaseModel
