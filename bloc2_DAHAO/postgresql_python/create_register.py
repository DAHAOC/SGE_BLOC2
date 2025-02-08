import connect

def create_reg():
    conn = connect.connection_db()

    cursor = conn.cursor()

    sql_create = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"

    values=('Roger', 'carrer el que sigui', '678113452', 'correu@correu.com', '12_09_1999')

    cursor.execute(sql_create, values)

    conn.commit()

    conn.close()
    cursor.close()


