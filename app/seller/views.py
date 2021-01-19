from flask import Blueprint, request, render_template, redirect

from app.seller.actions import create, read_all, read_by_id, delete, update
from app.seller.exceptions import SellerNotFoundException

seller = Blueprint(__name__, 'seller')


@seller.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@seller.route('/seller', methods=['GET'])
def seller_list():
    sellers = read_all()
    return render_template('seller/list.html', sellers=sellers)


@seller.route('/seller/create', methods=['GET'])
def seller_create_form():
    return render_template('seller/form.html')


@seller.route('/seller/create', methods=['POST'])
def seller_create():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    phone = request.form.get('phone')

    create(fullname, email, phone)

    return redirect('/seller')


@seller.route('/seller/update/<id>', methods=['GET'])
def seller_update_form(id: int):
    try:
        seller = read_by_id(id)
        return render_template('seller/form.html', seller=seller, update=True)
    except SellerNotFoundException:
        return redirect('/')


@seller.route('/seller/update/<id>', methods=['POST'])
def seller_update(id: int):
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    phone = request.form.get('phone')

    try:
        update(fullname, email, phone, id)
        return redirect('/seller')
    except SellerNotFoundException:
        return redirect('/')


@seller.route('/seller/delete/<id>', methods=['GET'])
def seller_delete(id: int):
    delete(id)
    return redirect('/seller')
