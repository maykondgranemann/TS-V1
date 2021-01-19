from flask import Flask, render_template

from back.models.seller_model import Seller
from back.models.product_model import Product
from back.models.marketplace_model import Marketplace
from back.models.category_model import Category

from back.controllers.seller_controller import SellerController
from back.controllers.product_controller import ProductController
from back.controllers.marketplace_controller import MarketplaceController
from back.controllers.category_controller import CategoryController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def read_products():
    result = ProductController().read_all()
    return render_template('product_read.html', products=result)

@app.route('/product/create')
def create_product():
    return render_template('product_create.html')

@app.route('/product/update')
def update_product():
    return render_template('product_update.html')

@app.route('/product/delete')
def delete_product():
    return render_template('product_delete.html')