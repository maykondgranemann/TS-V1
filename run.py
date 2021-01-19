from dotenv import load_dotenv
from backend.controllers.seller_controller import SellerController
from frontend.app.index import app

CONTROLLER = SellerController()

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
    result = CONTROLLER.read_all()


