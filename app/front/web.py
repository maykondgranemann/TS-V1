from datetime import datetime

from flask import Flask, render_template, request, redirect, flash
from app.back.utils import read_txt, write_to_logs


from app.back.marketplaces import create_marketplace, read_marketplaces
from app.back.products import create_product, read_products
from app.back.seller import create_seller, read_seller

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
    write_to_logs(f'marketplace listed - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
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

@app.route("/product/list")
def list_products():
    product_list = read_products()
    write_to_logs(f'product listed - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    return render_template("list_products.html", product_list=product_list)

@app.route("/log/list")
def list_log():
    log_list = read_txt("logs")
    
    return render_template("list_log.html", log_list=log_list)

@app.route('/seller/create')
def seller_create():
    if request.args:
        name =  request.args["name"],
        phone =  request.args.get('phone'),
        email = request.args.get('email')
        
        create_seller(name, phone, email)
        flash(f'Seller Created! - {name}')
        return redirect('/')
    
    return render_template("new_seller.html")

@app.route("/seller/list")
def list_sellers():
    seller_list = read_seller()
    write_to_logs(f'seller listed - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    return render_template("list_sellers.html", seller_list=seller_list)
