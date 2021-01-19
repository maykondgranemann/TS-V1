import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base= declarative_base()

class Seller(Base):
    __tablename__='seller'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(length=200))
    phone=db.Column(db.String(length=200))
    email=db.Column(db.String(length=200))
    
    def __str__(self):
        return f'ID:{self.id} / NAME:{self.name} / PHONE:{self.phone} / EMAIL:{self.email}'

def menu():

    print('-' * 20 + '\nSellers \n\n 1)Salvar\n', '2) Mostrar BD \n', '3) Atualizar\n',
          '4) Deletar\n', '5) Sair\n')

    op = int(input('Selecione uma opção: '))
    return op

def main():
    conector='postgresql'
    host='pgsql08-farm15.uni5.net'
    user='topskills7'
    password='olist21'
    database='topskills7'
    connection_string = f"{conector}://{user}:{password}@{host}:5432/{database}"

    engine=db.create_engine(connection_string)
    Session=sessionmaker(engine)
    session=Session()
        

    while True:
        op=menu()
        if op==1:
            seller_obj=Seller()
            seller_obj.email=input("Email:")
            seller_obj.name=input("Nome:")
            seller_obj.phone=input("TElefone:")
            session.add(seller_obj)
            session.commit()

        elif op==2:
            sellers=session.query(Seller).all()
            for s in sellers:
                print(s)

        elif op==3:
            id_aux=int(input("Digite o ID para atualizar:"))
            sellers=session.query(Seller).filter_by(id=id_aux).first()
            print(sellers)
            sellers.email=input("Email:")
            sellers.name=input("Nome:")
            sellers.phone=input("TElefone:")
            session.add(sellers)
            session.commit()
        
        elif op==4:
            id_aux=int(input("Digite o ID para deletar:"))
            sellers=session.query(Seller).filter_by(id=id_aux).first()
            session.delete(sellers)

main()