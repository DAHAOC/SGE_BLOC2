import psycopg2


def list_databases():
    try:
        conn = psycopg2.connect(
            database="the_bear",
            password="admin",
            user="admin",
            host="localhost",
            port="5432"
        )

        cursor = conn.cursor()

        # Consultar todas las bases de datos disponibles
        cursor.execute("SELECT datname FROM pg_database;")
        databases = cursor.fetchall()

        print("Bases de datos en el servidor:")
        for db in databases:
            print(db[0])
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cursor.fetchall()
        print("Tablas en the_bear:")
        for table in tables:
            print(table[0])

        cursor.close()
        conn.close()


    except Exception as e:
        print("Error en la conexión:", e)


list_databases()



