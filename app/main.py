from os import getenv
from uuid import uuid4

from flask import Flask

from app.seller.views import seller

app = Flask(__name__)
app.debug = True
app.secret_key = getenv('SECRET_KEY', str(uuid4()))

app.register_blueprint(seller)
