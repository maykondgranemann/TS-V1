import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Seller(Base):
    __tablename__ = 'seller'

    name = db.Column(db.String(length=200))
    phone = db.Column(db.String(length=200))
    email = db.Column(db.String(length=200))
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email


connector = 'postgresql'
host = 'pgsql08-farm15.uni5.net'
user = 'topskills3'
dbname = 'topskills3'
password = 'olist21'

conn_string = f"{connector}://{user}:{password}@{host}:5432/{dbname}"

engine = db.create_engine(conn_string)
Session = sessionmaker(engine)


def create_update(model: object):
    session = Session()
    session.add(model)
    session.commit()
    session.close()


def read_all() -> list:
    session = Session()
    sellers = session.query(Seller).all()
    session.close()
    return sellers


def read_by_id(id_):
    session = Session()
    sel = session.query(Seller).filter_by(id=id_).first()
    session.close()
    return sel


def delete(model: object):
    session = Session()
    session.delete(model)
    session.commit()
    session.close()


#testes

#create_update(Seller("Ana Paula", "12132312", "ana@teste.com"))

for i in read_all():
    print(i.name, i.phone, i.email, i.id)

seller = read_by_id(21)
print(seller.name, seller.id, seller.email)

#seller.name = "novo seller"
#seller.email = "new@seller.com"

#create_update(seller)

#delete(seller)
