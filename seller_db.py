import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Seller(Base):
    __tablename__ = 'sellers'
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String(length=200) )
    phone = db.Column( db.String(length=50) )
    email = db.Column( db.String(length=200) )

    def __repr__(self):
        return f'{self.id}-{self.name}-{self.phone}-{self.email}'

sql = 'postgresql'
host = 'pgsql08-farm15.uni5.net'
user = 'topskills13'
password = 'olist123'
database = 'topskills13'
conn_string = f"{sql}://{user}:{password}@{host}:5432/{database}"

engine = db.create_engine(conn_string)
Session = sessionmaker(engine)
session = Session()

new_seller = Seller()
new_seller.name = 'Marcos Doug'
new_seller.phone = '(94) 98888-7777'
new_seller.email = 'contato@olist.com'

session.add(new_seller)
session.commit()

sellers = session.query(Seller).all()
print(sellers)
