from backend.models.base_model import BaseModel



class TestBaseModel:

    def test_base_model(self):
        test_bmodel = BaseModel()
        assert isinstance(test_bmodel, BaseModel)


def start_test_bmodel():
    tmodel = TestBaseModel()
    tmodel.test_base_model()





