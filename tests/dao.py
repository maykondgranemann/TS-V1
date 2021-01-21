import sys
sys.path.append('/teste/')
from models.seller import Seller
from dao.base import BaseDao
from dao.seller import SellerDao
from dao.session import Session

# Base
name = 'Clara'
email = 'clara@olist.com'
phone = '(47) 9 8745-4324'
seller = Seller(name, email, phone)

base = BaseDao(Seller)
assert base.save(seller) == None

sellers = base.read_all()
assert isinstance(sellers, list)
assert isinstance(sellers[0], object)

sel = base.read_by_id(0)
assert isinstance(sel, object)

assert base.save(sel) == None
assert base.delete(seller) == None

# Seller
seller = SellerDao()
assert seller.add(sel) == None
assert isinstance(seller.read_all(), list)
assert isinstance(seller.read_by_id(0), object)
sel = seller.read_by_id(0)
sel.name = 'Cla'
sel.email = '(47) 9 4542-4566'
assert seller.add(sel) == None
assert seller.delete(sel) == None

# Session