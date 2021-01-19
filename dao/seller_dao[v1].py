from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
import sys
sys.path.append('.')


# declaração das variaveis de
# conexão com o bd
connector = 'postgresql'  # define qual o tipo de banco você está utilizando
# desta forma é possível alterar o tipo de banco
# sem realizar muitas alterações no código
host = 'pgsql08-farm15.uni5.net'
user = 'topskills13'
password = 'olist123'
dbname = 'topskills13'

# declaração obrigatoria
base = declarative_base()


class Seller(base):
    # atributo obrigatorio, define qual tabela
    # o alchemy deve utilizar
    __tablename__ = 'sellers'
    # abaixo segue as declarações das colunas do bd
    # e seus tipos
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50))
    phone = db.Column(db.String(length=50))
    email = db.Column(db.String(length=50))


# criaçao da connection string
# postgresql://topskills13:olist123@pgsql08-farm15.uni5.net:5432/topskills13
conn_string = f"{connector}://{user}:{password}@{host}:5432/{dbname}"

# ponto de partida de qualquer aplicação SQLAlchmy,
# realiza a conexão com a base ou api - https://docs.sqlalchemy.org/en/14/core/engines.html
engine = db.create_engine(conn_string)

# session estabele uma comunicação com a base
# e se comporta como um 'zona de espera' durante sua vida util
# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
Session = sessionmaker(engine)

# Estou instânciando uma nova sessão
session = Session()

# Estou instânciando um objeto do tipo Seller
obj_seller = Seller()

# Carrego os dados no objeto instanciado acima
obj_seller.name = 'Ponto do eletro'
obj_seller.phone = '(55)+41 99999-9999'
obj_seller.email = 'pe@pe.com.br'

############INSERT###################
# estou enviando o objeto preenchido
# para zona de espera da session
# session.add(obj_seller)

# estou efetivando (commit) os comandos
# que estão na zona de espera da session
# session.commit()

############SELECT###################
# recuperar todos os registros da tabela
result = session.query(Seller).all()

# mostrar o resultado recuperado
for item in result:
    print(item.id, item.name, item.phone, item.email)

############UPDATE###################
# para realizar o update é precisa passar o objeto 'Seller'
# para o sqlalchemy
obj = result[0]  # vou pegar o primeiro objeto retornado do select
# após recuperar o objeto, altere as informações necessárias
# e envie para zona de espera
#obj.name = 'José da Padaria'
#obj.phone = '(55)+41 8888-8888'
# para atualizar é utilizado o mesmo comando do insert
# session.add(obj)
# session.commit()

############DELETE###################
# para realizar o delete é precisa passar o objeto 'Seller'
# para o sqlalchemy
# obj = result[0]
# session.delete(obj)
# session.commit()
