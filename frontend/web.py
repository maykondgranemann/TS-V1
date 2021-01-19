from flask import Flask, render_template, request,redirect
import sys

from sqlalchemy.orm import backref
sys.path.append('.')

from backend.controller.seller_controller import SellerController
from backend.models.seller import Seller

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listseller')
def list_categories():
    sellers = SellerController().listall()
    return render_template('listseller.html', seller=sellers)


@app.route('/createseller')
def create_seller():
    return render_template('createseller.html')


@app.route('/seller')
def save_seller():
    name = request.args.get('name')
    phone = request.args.get('phone')
    email = request.args.get('email')
    seller = Seller(name, email, phone)
    SellerController().create(seller)
    return render_template('success.html')

@app.route('/delete_seller')
def delete_seller():
    id = int(request.args.get('id'))
    seller = SellerController().read_id(id)
    SellerController().delete_seller(seller)
    return redirect('/listseller')  

@app.route('/update_seller')
def update_seller():
    id = request.args.get('id')
    s = SellerController().read_id(id)
    return render_template('createseller.html', update=True, id=s.id, name=s.name, email=s.email, phone=s.phone)  


@app.route('/update_seller', methods=['POST'])
def save_update_seller():
    return redirect('/listseller')      

app.run(debug=True)