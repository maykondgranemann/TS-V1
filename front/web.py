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
    return render_template('product_read.html')

@app.route('/product/create')
def create_product():
    return render_template('product_create.html')

@app.route('/product/<id>/update')
def update_product():
    return render_template('product_update.html')

@app.route('/product/<id>/delete')
def delete_product():
    return render_template('product_delete.html')



seller = Seller('Lucas', '219999999999', 'lucas@olist.com')

SellerController().create(seller)

seller = SellerController().read_by_id(46)

print(seller)

seller.name = "Lucas João"

SellerController().update(seller)

seller = SellerController().read_by_id(46)

print(seller)

#SellerController().delete(seller)

sellers = SellerController().read_all()

for s in sellers:
    print(s)
