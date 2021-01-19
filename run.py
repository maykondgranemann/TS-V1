from dotenv import load_dotenv

from app.database.models import Base
from app.database.session import Session
from app.main import app

from app.seller.models import Seller

if __name__ == '__main__':
    load_dotenv()
    Base.metadata.create_all(Session().get_engine())
    app.run()
