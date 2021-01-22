from ATV_Ana.back.models.seller import Seller

sel = Seller('Ana', '12323324235', 'teste@xp.com')

assert sel.name == 'Ana'
assert isinstance(sel.name, str)

assert sel.phone == '12323324235'
assert isinstance(sel.phone, str)

assert sel.email == 'teste@xp.com'
assert isinstance(sel.email, str)


try:
    sel = Seller('3232', '43141341', 'teste@xp.com')
except Exception as e:
    assert isinstance(e, ValueError)

try:
    sel = Seller('teste', 'dasdasda', 'teste@xp.com')
except Exception as e:
    assert isinstance(e, ValueError)

try:
    sel = Seller('teste', '41231231', 'testep.com')
except Exception as e:
    assert isinstance(e, ValueError)