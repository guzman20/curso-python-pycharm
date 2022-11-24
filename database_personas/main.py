from Utils.conexiones import get_mysql_conection


def insertar():
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellidos, email) VALUES(%s, %s, %s)'
            valores = (
                ('Pablo', "Gonzalez", "pablo.gonzalez@gmail.com"),
                ('Maria', "Fernandez", "maria_F2000@outlook.com"),
                ('Pedro', "Hernandez", "pehe1996@correos.com")
            )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')


def select():
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT nombre FROM personas'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)


def select_gmail():
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM personas WHERE email LIKE %s"
            cursor.execute(sentencia, ["%@gmail"])
            registros = cursor.fetchall()
            print(registros)
        cursor.close()
    conexion.close()


def update_gmail():
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE personas SET email = (SELECT * FROM personas)@gmail.com WHERE email not like ' \
                        '"%gmail.com" '
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
            cursor.close()
    conexion.close()


if __name__ == '__main__':

    try:
        # insertar()
        # select()
        select_gmail()
        # update_gmail()
    except Exception as e:
        print(f'Ocurrió un error: {e}')
