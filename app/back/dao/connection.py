import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills12'
_password = 'olist21'
_database = 'topskills12'

_connection_string = f'host={_host} user={_user} dbname = {_database} password={_password}'

def _set_database():
    conn = psycopg2.connect(_connection_string)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS product (id serial not null, name varchar(200) not null, phone varchar(20) not null, mail varchar(50) not null, constraint product_pk primary key (id)) ;")
    cur.execute("CREATE TABLE IF NOT EXISTS category (id serial not null, name varchar(200) not null, description varchar(20) not null, constraint category_pk primary key (id)) ;")
    cur.execute("CREATE TABLE IF NOT EXISTS marketplace (id serial not null, name varchar(50) not null, description varchar(200) null, constraint marketplace_pk primary key (id));")
    cur.execute("CREATE TABLE IF NOT EXISTS seller (id serial not null, name varchar(100) not null, telephone varchar(20) not null, email varchar(50) not null, constraint seller_pk primary key (id));")
    cur.execute("CREATE TABLE IF NOT EXISTS log (id serial not null, message varchar(50) not null, constraint log_pk primary key (id));")
    conn.commit()

    cur.close()
    conn.close()

def get_connection():
    _set_database()
    return psycopg2.connect(_connection_string)
