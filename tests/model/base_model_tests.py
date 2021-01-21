import sys
sys.path.append('')
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

#Teste#
if id == Integer:
    try:
        print('Ok')
    except Exception as error:
        assert isinstance(error, TypeError)