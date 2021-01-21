# importar Column e Integer
# importar declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Criar variável que receba a função declarative_base
Base = declarative_base()

# A model_base deverá conter qualquer informação que possa ser 
# comum em outras models, neste caso o ID
class BaseModel(Base):

# Criar o abstract para corrigir conflito de tabela
    __abstract__ = True
    
# Declarar a ID como coluna no BD
    id = Column( Integer, primary_key=True )
