import psycopg2


_file_name = 'app/back/dao/credentials.txt'

def get_credential() -> list:
    credentials = []
    file = open(_file_name, 'r')
    for line in file:
        treated_line = line.strip()
        credentials.append(treated_line)
    file.close()
    return credentials

def _connection_credentials() -> str:
    credentials = get_credential()
    host = credentials[0]
    user = credentials[1]
    database = credentials[2]
    password = credentials[3]
    return f'host={host} user={user} dbname={database} password={password}'

def _set_database():
    conn = psycopg2.connect(_connection_credentials())
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS product (id serial not null, name varchar(200) not null, description varchar(200) not null, price numeric(20) not null, constraint product_pk primary key (id)) ;")
    cur.execute("CREATE TABLE IF NOT EXISTS category (id serial not null, name varchar(200) not null, description varchar(200) not null, constraint category_pk primary key (id)) ;")
    cur.execute("CREATE TABLE IF NOT EXISTS marketplace (id serial not null, name varchar(50) not null, description varchar(200) null, constraint marketplace_pk primary key (id));")
    cur.execute("CREATE TABLE IF NOT EXISTS seller (id serial not null, name varchar(100) not null, telephone varchar(20) not null, email varchar(50) not null, constraint seller_pk primary key (id));")
    cur.execute("CREATE TABLE IF NOT EXISTS log (id serial not null, message varchar(500) not null, constraint log_pk primary key (id));")
    conn.commit()

    cur.close()
    conn.close()

def get_connection():
    _set_database()
    return psycopg2.connect(_connection_credentials())
