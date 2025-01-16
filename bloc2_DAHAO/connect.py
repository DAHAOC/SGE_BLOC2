import psycopg2

def connection_db():
    conn = psycop2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )
    return conn
