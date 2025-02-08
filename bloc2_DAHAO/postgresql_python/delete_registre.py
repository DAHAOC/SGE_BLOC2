import connect

def delete_rug():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_delete = '''
    DELETE FROM clientes
    WHERE nombre_cliente = 'Roger';
    '''

    cursor.execute(sql_delete)
    conn.commit()

    conn.close()
    cursor.close()
    return {"Delete successfully"}

print(delete_rug())