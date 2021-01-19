# Importar do sqlalchemy create_engine e sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Criar uma classe de conexão vinculada ao BD
class Session:
    def __init__(self):

# Referenciar BD no conector diferente da atividade anterior
        conector = 'postgres'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills3'
        dbname = 'topskills3'
        password = 'olist21'

# A conn_string também segue uma estrutura diferente
# A mesma deve apontar o conector ao ususário depois pass at host a porta e o nome do BD
        conn_string = f"{conector}://{user}:{password}@{host}:5432/{dbname}"

# Criar uma função de inicialização com __enter__
    def __enter__(self):
        pass

# Criar uma função de fechamento de conexaõ com __exit__
# Esta deverá conter .dispose() e .close()
    def __exit__(self, type, value, trace):
        pass
