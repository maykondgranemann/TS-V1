from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
