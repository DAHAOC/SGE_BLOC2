import psycopg2

def create_tables():
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            database="the_bear",
            user="admin",
            password="admin",
            host="localhost",
            port="5432"
        )

        cursor = conn.cursor()

        # Consulta para crear la tabla
        sql_clients = '''
        CREATE TABLE IF NOT EXISTS Clientes (
            Nombre_Cliente VARCHAR(100),
            Dirección_Cliente VARCHAR(200),
            Teléfono_Cliente VARCHAR(100),
            Correo_Electrónico_Cliente VARCHAR(100),
            Fecha_Cumpleaños VARCHAR(50)
        );
        '''

        # Ejecutar la consulta para crear la tabla
        cursor.execute(sql_clients)
        conn.commit()

        print("Tabla 'Clientes' creada correctamente.")  # Mensaje de éxito

    except Exception as e:
        print("Error al crear la tabla:", e)  # Capturar y mostrar errores

    finally:
        # Cerrar conexión y cursor
        cursor.close()
        conn.close()

    return {"Tables created successfully"}

# Llamar a la función para crear la tabla
create_tables()
