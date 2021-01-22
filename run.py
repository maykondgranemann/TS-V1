from tests.model.seller_test import start_all_model
from tests.model.base_test import start_all_base_model
from tests.dao.seller_test import start_all_dao
from tests.dao.base_test import start_all_base_dao
from tests.controller.seller_test import start_all_controller
from tests.controller.base_test import start_all_base_controller

start_all_base_model()
start_all_base_dao()
start_all_base_controller()
start_all_model()
start_all_dao()
start_all_controller()
