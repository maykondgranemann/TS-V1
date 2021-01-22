from flask import request, render_template, Blueprint, redirect
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller

seller = Blueprint(__name__, 'seller')
CONTROLLER = SellerController()


@seller.route('/sellers')
def list_all_sellers():
    sellers = CONTROLLER.read_all()
    return render_template('seller.html', name='olist', sellers=sellers)


@seller.route('/sellers/create')
def create_seller_form():
    return render_template('seller_form.html', name='olist')


@seller.route('/sellers/create', methods=['POST'])
def create_seller():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    phone = request.form.get('phone_number')
    new_seller = Seller(fullname, phone, email)
    print(fullname, email, phone)
    if (fullname is None) and (email is None) and (phone is None):
        return render_template('seller_form.html', name='olist')
    else:
        CONTROLLER.save(new_seller)
        return redirect('/sellers')


@seller.route('/sellers/update')
def update_get():
    id_ = request.args.get('id')
    seller = CONTROLLER.read_by_id(id_)
    return render_template('seller_form.html', name='olist', edit=True, seller=seller)


@seller.route('/sellers/update', methods=['POST'])
def update_post():
    id_ = request.form.get('id')
    seller = CONTROLLER.read_by_id(id_)
    seller.fullname = request.form.get('fullname')
    seller.email = request.form.get('email')
    seller.phone = request.form.get('phone_number')
    CONTROLLER.save(seller)
    return redirect('/sellers')


@seller.route('/sellers/delete')
def delete():
    id_ = request.args.get('id')
    seller = CONTROLLER.read_by_id(id_)
    CONTROLLER.delete(seller)
    return redirect('/sellers')
