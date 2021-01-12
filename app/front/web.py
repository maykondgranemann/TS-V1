from datetime import datetime

from flask import Flask, render_template, request, redirect, flash

from app.back.controllers.category_controller import create_category, read_categories
from app.back.controllers.marketplace_controller import create_marketplace, read_marketplace
from app.back.controllers.product_controller import create_product, read_products
from app.back.controllers.log_controller import create_log, read_logs
from app.back.controllers.seller_controller import create_seller, read_seller
from app.back.models.product import Product
from app.back.models.category import Category
from app.back.models.seller import Seller
from app.back.models.marketplace import Marketplace

app = Flask(__name__)
app.secret_key = 'IOAHGFYAOGFEYHAGO'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/marketplace')
def marketplace_form():
    return render_template('new_marketplace.html')


@app.route('/marketplace/create')
def marketplace_create():
    name = request.args.get('name')
    description = request.args.get('description')
    marketplace = Marketplace(name, description)
    create_marketplace(marketplace)
    flash(f'Marketplace Created! - {name}')
    return redirect('/')


@app.route('/marketplace/list')
def marketplace_read():
    list_marketplaces = read_marketplace()
    return render_template('list_marketplaces.html', list=list_marketplaces)


@app.route('/product')
def product_form():
    return render_template('new_product.html')


@app.route('/product/create')
def product_create():
    name = request.args.get('name')
    description = request.args.get('description')
    price = float(request.args.get('price'))
    product = Product(name, description, price)
    create_product(product)
    flash(f'Product Created! - {product.name}')
    return redirect('/')


@app.route("/product/list")
def list_products():
    product_list = read_products()
    return render_template("list_products.html", product_list=product_list)


@app.route('/category')
def category_form():
    return render_template('new_category.html')


@app.route('/category/create')
def category_create():
    name = request.args.get('name')
    description = request.args.get('description')
    category= Category(name, description)
    create_category(category)
    flash(f'Category Created! - {category.name}')
    return redirect('/')


@app.route('/category/list')
def category_read():
    list_categories = read_categories()
    return render_template('list_categories.html', list=list_categories)


@app.route("/log/list")
def list_log():
    log_list = read_logs()
    return render_template("list_log.html", log_list=log_list, color= "")


@app.route('/seller')
def seller_form():
    return render_template("new_seller.html")


@app.route('/seller/create')
def seller_create():
    name =  request.args.get('name')
    phone =  request.args.get('phone')
    email = request.args.get('email')
    seller = Seller(name, phone, email)
    create_seller(seller)
    flash(f'Seller Created! - {name}')
    return redirect('/')


@app.route("/seller/list")
def list_sellers():
    seller_list = read_seller()
    return render_template("list_sellers.html", seller_list=seller_list)
