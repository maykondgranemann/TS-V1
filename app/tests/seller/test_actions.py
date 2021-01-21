from app.seller.actions import create, read_all


def test_read_all_should_fetch_from_db():
    result = read_all()

    assert isinstance(result, list)


def test_create_should_save_to_db():
    fullname = 'fullname'
    email = 'mail@test.com'
    phone = '99999999999'

    create(fullname, email, phone)

    result = read_all()[-1]

    assert fullname == result.fullname
    assert email == result.email
    assert phone == result.phone
