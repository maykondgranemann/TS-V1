from flask import Flask, render_template, request, redirect, flash

from app.back.categories import create_category, read_categories
from app.back.marketplaces import create_marketplace, read_marketplaces
from app.back.products import create_product, read_products

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
    create_marketplace(name, description)
    flash(f'Marketplace Created! - {name}')
    return redirect('/')


@app.route('/marketplace/list')
def marketplace_read():
    list_marketplaces = read_marketplaces()
    return render_template('list_marketplaces.html', list=list_marketplaces)


@app.route('/product')
def product_form():
    return render_template('new_product.html')


@app.route('/product/create')
def product_create():
    name = request.args.get('name')
    description = request.args.get('description')
    price = float(request.args.get('price'))
    create_product(name, description, price)
    flash(f'Product Created! - {name}')
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
    create_category(name, description)
    flash(f'Category Created! - {name}')
    return redirect('/')


@app.route('/category/list')
def category_read():
    list_categories = read_categories()
    return render_template('list_categories.html', list=list_categories)
