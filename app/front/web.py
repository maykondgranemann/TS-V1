from flask import Flask, render_template, request, redirect, flash


from app.back.marketplaces import create_marketplace, read_marketplaces
from app.back.products import create_product


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
    return render_template('read_marketplaces.html', list = list_marketplaces)


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
