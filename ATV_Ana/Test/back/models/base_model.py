from ATV_Ana.back.models.base_model import BaseModel

bm = BaseModel()

bm.id = 321

assert bm.id == 321

assert isinstance(bm.id, int)

assert isinstance(bm, BaseModel)