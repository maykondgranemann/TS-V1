from flask import request, render_template, Blueprint, redirect
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller

seller = Blueprint(__name__, 'seller')
CONTROLLER = SellerController()


@seller.route('/sellers')
def list_all_sellers():
    sellers = CONTROLLER.read_all()
    return render_template('seller.html', name='olist', sellers=sellers)


@seller.route('/sellers/update')
def update_get():
    id_ = request.args.get('id')
    seller = CONTROLLER.read_by_id(id_)
    return render_template('seller_form.html', name='olist', edit=True, seller=seller)


@seller.route('/sellers/update', methods=['POST'])
def update_post():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    phone = request.form.get('phone_number')
    seller = Seller(fullname, phone, email)
    CONTROLLER.save(seller)
    return redirect('/sellers')
