import random

from Exceptions.AfinadoException import AfinadoException
from Utils.Log_orquesta import log


class Instrumento:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__afinado = False

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_afinado(self):
        return self.__afinado

    def set_afinado(self, afinado):
        self.__afinado = afinado

    def afinar(self):
        afinado = random.randint(0, 1)
        if afinado == 0:
            self.set_afinado(True)
            log.info("El instrumento {} ha sido afinado".format(self.get_nombre))
        else:
            self.set_afinado(False)
            log.info("El instrumento {} no se ha afinado".format(self.get_nombre))

    def tocar(self):
        if self.get_afinado():
            log.info("El instrumento {} esta sonando".format(self.get_nombre))
            return "El instrumento {} esta sonando".format(self.get_nombre)
        else:
            log.error("El instrumento {} no esta afinado y sonó mal".format(self.get_nombre))
            raise AfinadoException()
