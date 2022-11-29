import os

from Entidades.Apostante import Apostante
from Entidades.Caballo import Caballo
from Entidades.Gran_premio import Gran_premio
from Utils.bdd.conexiones import get_mysql_conection

SEPARADOR = "|"
NOMBRE = 0


def subir(fichero_nombre, objeto_tipo):
    elementos = []
    fichero = os.getcwd() + '/Utils/datos_ficheros/' + fichero_nombre + '.txt'
    archivo = open(fichero, 'r')

    if objeto_tipo == "apostantes":
        SALDO = 1
        for linea in archivo:
            palabras = linea.split(SEPARADOR)
            elementos.append(Apostante(None, palabras[NOMBRE], int(palabras[SALDO].rstrip('\n'))))

    elif objeto_tipo == "caballos":
        FECHA_NACIMIENTO = 1
        VELOCIDAD = 2
        EXPERIENCIA = 3
        VALOR_APUESTA = 4
        GRANPREMIO = 5
        for linea in archivo:
            palabras = linea.split(SEPARADOR)
            elementos.append(Caballo(None, palabras[NOMBRE], palabras[FECHA_NACIMIENTO], int(palabras[VELOCIDAD])
                                     , int(palabras[EXPERIENCIA]), int(palabras[VALOR_APUESTA])
                                     , int(palabras[GRANPREMIO].rstrip('\n'))))

    elif objeto_tipo == "gran_premio":
        DISTANCIA = 1
        NUM_CARRERAS = 2
        for linea in archivo:
            palabras = linea.split(SEPARADOR)
            elementos.append(Gran_premio(None, palabras[NOMBRE], palabras[DISTANCIA]
                                         , palabras[NUM_CARRERAS].rstrip('\n')))
    else:
        raise IOError
    return elementos


def actualizar_elementos(lista, tabla):
    pass
