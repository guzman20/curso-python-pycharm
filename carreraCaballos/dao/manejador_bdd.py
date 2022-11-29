from Utils.bdd.conexiones import get_mysql_conection


def subir_elementos(lista, tabla):
    valores = []
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            if tabla is "apostantes":
                sentencia = 'INSERT INTO apostantes (nombre, saldo) VALUES(%s, %s)'
                for elemento in lista:
                    valores.append((elemento.nombre, elemento.saldo))
            elif tabla is "caballos":
                sentencia = 'INSERT INTO caballos (nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta' \
                            ', id_gran_premio) VALUES(%s, %s, %s, %s, %s, %s)'
                for elemento in lista:
                    valores.append((elemento.nombre, elemento.fecha_nacimiento, elemento.velocidad, elemento.experiencia
                                    , elemento.valor_apuesta, elemento.gran_premio))
            elif tabla is "gran_premio":
                sentencia = 'INSERT INTO gran_premio (nombre, distancia, num_carreras) VALUES(%s, %s, %s)'
                for elemento in lista:
                    valores.append((elemento.nombre, elemento.distancia, elemento.num_carreras))
            else:
                raise ReferenceError("La tabla {} no existe".format(tabla))

            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')