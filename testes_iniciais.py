import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
'''
Base = declarative_base()


class Seller(Base):
    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=200))
    phone = db.Column(db.String(length=11))
    email = db.Column(db.String(length=200))

conector = 'postgresql'
host = 'pgsql08-farm15.uni5.net'
user = 'topskills9'
password = 'olist123'
dbname = 'topskills9'
conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"

engine = db.create_engine(conn_string)
Session = sessionmaker(engine)
session = Session()

sellers = session.query(Seller).all()
for s in sellers:
    print(s.name)

'''
'''
PG_HOST=pgsql08-farm15.uni5.net
PG_USER=topskills9
PG_PASSWORD=olist123
PG_DATABASE=topskills9
'''
