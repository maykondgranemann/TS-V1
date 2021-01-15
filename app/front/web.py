from app.back.controllers.log_controller import LogController
from flask import Flask, render_template, request, redirect, flash

from app.back.controllers.marketplace_controller import MarketplaceController
from app.back.controllers.log_controller import LogController
from app.back.controllers.seller_controller import SellerController
from app.back.controllers.category_controller import CategoryController
from app.back.controllers.product_controller import ProductController
from app.back.models.product import Product
from app.back.models.category import Category
from app.back.models.seller import Seller
from app.back.models.marketplace import Marketplace

app = Flask(__name__)
app.secret_key = 'IOAHGFYAOGFEYHAGO'

category_controller = CategoryController("category")
product_controller = ProductController("product")
seller_controller = SellerController("seller")
marketplace_controller = MarketplaceController("marketplace")
log_controller = LogController()

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
    marketplace_controller.create(marketplace)
    flash(f'Marketplace Created! - {name}')
    return redirect('/')
    
@app.route('/marketplace/update/form')
def marketplace_update_form():
    id = request.args.get('id')
    marketplace = marketplace_controller.read_by_id(id)
    return render_template("update_marketplace.html", marketplace=marketplace)

@app.route('/marketplace/update')
def marketplace_update():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    marketplace = Marketplace(name, description, id)
    marketplace_controller.update(marketplace)
    return redirect("/marketplace/list")

@app.route('/marketplace/delete')
def marketplace_delete():
    id = request.args.get('id')
    marketplace_controller.delete(id)
    return redirect("/marketplace/list")

@app.route('/marketplace/list')
def marketplace_read():
    list_marketplaces = marketplace_controller.read_all()
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
    product_controller.create(product)
    flash(f'Product Created! - {product.name}')
    return redirect('/')


@app.route('/product/update')
def product_update_form():
    id = request.args.get('id')
    product = product_controller.read_by_id(id)
    return render_template('update_product.html', product=product)


@app.route('/product/updated')
def product_update():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    price = float(request.args.get('price'))
    
    product= Product(name, description, price, id)
    product_controller.update(product)
    flash(f'Product Updated! - {product.name}')
    return redirect('/product/list')


@app.route('/product/delete')
def product_delete():
    id = request.args.get('id')

    product_controller.delete(id)
    flash(f'Product Deleted!')
    return redirect('/product/list')


@app.route("/product/list")
def list_products():
    product_list = product_controller.read_all()
    return render_template("list_products.html", product_list=product_list)


@app.route('/category')
def category_form():
    return render_template('new_category.html')


@app.route('/category/create')
def category_create():
    name = request.args.get('name')
    description = request.args.get('description')
    category= Category(name, description)
    category_controller.create(category)
    flash(f'Category Created! - {category.name}')
    return redirect('/')


@app.route('/category/update')
def category_update_form():
    id = request.args.get('id')
    category = category_controller.read_by_id(id)
    return render_template('update_category.html', category=category)


@app.route('/category/updated')
def category_update():
    id = request.args.get('id')
    name = request.args.get('name')
    description = request.args.get('description')
    
    category= Category(name, description, id)
    category_controller.update(category)

    flash(f'Category Updated! - {category.name}')
    return redirect('/category/list')


@app.route('/category/delete')
def category_delete():
    id = request.args.get('id')

    category_controller.delete(id)
    flash(f'Category Deleted!')
    return redirect('/category/list')


@app.route('/category/list')
def category_read():
    list_categories = category_controller.read_all()
    return render_template('list_categories.html', list=list_categories)


@app.route("/log/list")
def list_log():
    log_list = log_controller.read_all()
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
    seller_controller.create(seller)
    flash(f'Seller Created! - {name}')
    return redirect('/')


@app.route("/seller/list")
def list_sellers():
    seller_list = seller_controller.read_all()
    return render_template("list_sellers.html", seller_list=seller_list)

@app.route('/seller/update/form')
def seller_update_form():
    id = request.args.get('id')
    seller = seller_controller.read_by_id(id)
    return render_template("update_seller.html", seller=seller)

@app.route('/seller/update')
def seller_update():
    id = request.args.get('id')
    name = request.args.get('name')
    telephone = request.args.get('telephone')
    email = request.args.get('email')
    seller = Seller(name, telephone, email, id)
    seller_controller.update(seller)
    return redirect('/seller/list')

@app.route('/seller/delete')
def seller_delete():
    id = request.args.get('id')
    seller_controller.delete(id)
    return redirect("/seller/list")
