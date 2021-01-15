import psycopg2

class Connection:
    def __get_credential(self) -> list:
        _file_name = 'app/back/dao/credentials.txt'
        credentials = []
        
        with open(_file_name, 'r') as file:
            for line in file:
                treated_line = line.strip()
                credentials.append(treated_line)
        return credentials

    def __connection_credentials(self) -> str:
        credentials = self.__get_credential()
        host = credentials[0]
        user = credentials[1]
        database = credentials[2]
        password = credentials[3]
        return f'host={host} user={user} dbname={database} password={password}'

    def __enter__(self):
        self.__connection = psycopg2.connect(self.__connection_credentials())
        return self.__connection

    def __exit__(self, type, value, trace):
        self.__connection.close()

    def set_database(self):
        try:
            with psycopg2.connect(self.__connection_credentials()) as conn:
                cur = conn.cursor()

                cur.execute("CREATE TABLE IF NOT EXISTS product (id serial not null, name varchar(200) not null, description varchar(200) not null, price numeric(20) not null, constraint product_pk primary key (id)) ;")
                cur.execute("CREATE TABLE IF NOT EXISTS category (id serial not null, name varchar(200) not null, description varchar(200) not null, constraint category_pk primary key (id)) ;")
                cur.execute("CREATE TABLE IF NOT EXISTS marketplace (id serial not null, name varchar(50) not null, description varchar(200) null, constraint marketplace_pk primary key (id));")
                cur.execute("CREATE TABLE IF NOT EXISTS seller (id serial not null, name varchar(100) not null, telephone varchar(20) not null, email varchar(50) not null, constraint seller_pk primary key (id));")
                cur.execute("CREATE TABLE IF NOT EXISTS log (id serial not null, message varchar(500) not null, constraint log_pk primary key (id));")
                conn.commit()
        except:
            print('An unexpected error has occurred')
