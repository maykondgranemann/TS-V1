import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller


app = Flask(__name__)
seller_controller = SellerController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sellers', methods=["GET", "POST"])
def list_sellers():
    if request.method == "POST":
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        seller = Seller(name, phone, email)
        seller_controller.create(seller)
    sellers = seller_controller.read_all()
    return render_template('list_sellers.html', sellers=sellers)

@app.route('/create_seller')
def new_seller():
    return render_template('create_seller.html')

@app.route('/sellers/<int:id>', methods=['GET', 'POST'])
def edit_seller(id: int):
    seller = seller_controller.read_by_id(id)
    if request.method == "POST":
        seller.name = request.form.get('name')
        seller.phone = request.form.get('phone')
        seller.email = request.form.get('email')
        seller_controller.update(seller)
        return redirect(url_for('list_sellers'))
    return render_template('edit_seller.html', seller=seller)

@app.route('/sellers/<int:id>/delete', methods=['GET'])
def delete_seller(id: int):
    seller = seller_controller.read_by_id(id)
    seller_controller.delete(seller)
    return redirect(url_for('list_sellers'))

app.run(debug=True)
