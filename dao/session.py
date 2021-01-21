# Importar do sqlalchemy create_engine e sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Criar uma classe de conexão vinculada ao BD
class Session:
    def __init__(self) -> None:

# Referenciar BD no conector diferente da atividade anterior
        conector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills3'
        password = 'olist21'
        dbname = 'topskills3'
        
# A conn_string também segue uma estrutura diferente
# A mesma deve apontar o conector ao ususário depois pass at host a porta e o nome do BD
# Estabelecendo a conexão como privada no através do self
        self.__conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"

# Criar uma função de inicialização com __enter__
    def __enter__(self) -> object:
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

# Criar uma função de fechamento de conexaõ com __exit__
# Esta deverá conter .dispose() e .close()
    def __exit__(self, type, value, traceback) -> None:
        self.__session.close()
        self.__engine.dispose()
