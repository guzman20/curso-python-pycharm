import os

from Classes.Apostante import Apostante
from Classes.Caballo import Caballo
from Classes.Gran_premio import Gran_premio
from Utils.bdd.conexiones import get_mysql_conection

SEPARADOR = "|"
NOMBRE = 0


def cargar(fichero_nombre, tabla):
    elementos = []
    valores = []
    fichero = "Utils/ficheros/" + fichero_nombre + '.txt'
    archivo = open(fichero, 'r')
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            if tabla == "apostantes":
                SALDO = 1
                for linea in archivo:
                    palabras = linea.split(SEPARADOR)
                    elementos.append(Apostante(None, palabras[NOMBRE], palabras[SALDO].rstrip('\n')))
                sentencia = 'INSERT INTO apostantes (nombre, saldo) VALUES(%s, %s)'
                for elemento in elementos:
                    valores.append((elemento.nombre, elemento.saldo))

            elif tabla == "caballos":
                FECHA_NACIMIENTO = 1
                VELOCIDAD = 2
                EXPERIENCIA = 3
                VALOR_APUESTA = 4
                GRANPREMIO = 5
                for linea in archivo:
                    palabras = linea.split(SEPARADOR)
                    elementos.append(Caballo(None, palabras[NOMBRE], palabras[FECHA_NACIMIENTO], palabras[VELOCIDAD]
                                             , palabras[EXPERIENCIA], palabras[VALOR_APUESTA]
                                             , palabras[GRANPREMIO].rstrip('\n')))
                sentencia = 'INSERT INTO caballos (nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta' \
                            ', id_gran_premio) VALUES(%s, %s, %s, %s, %s, %s)'
                for elemento in elementos:
                    valores.append((elemento.nombre, elemento.fecha_nacimiento, elemento.velocidad, elemento.experiencia
                                    , elemento.valor_apuesta, elemento.gran_premio))

            elif tabla == "gran_premio":
                DISTANCIA = 1
                NUM_CARRERAS = 2
                for linea in archivo:
                    palabras = linea.split(SEPARADOR)
                    elementos.append(Gran_premio(None, palabras[NOMBRE], palabras[DISTANCIA]
                                                 , palabras[NUM_CARRERAS].rstrip('\n')))
                sentencia = 'INSERT INTO gran_premio (nombre, distancia, num_carreras) VALUES(%s, %s, %s)'
                for elemento in elementos:
                    valores.append((elemento.nombre, elemento.distancia, elemento.num_carreras))
            else:
                raise IOError

            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
