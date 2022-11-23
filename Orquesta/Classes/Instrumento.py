import random
from abc import ABC

from Exceptions.AfinadoException import AfinadoException
from Utils.Log_orquesta import log
from decoradores.decorador_orquesta import log_orquesta


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo
        self._afinado = False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def afinado(self):
        return self._afinado

    @afinado.setter
    def afinado(self, afinado):
        self._afinado = afinado

    @log_orquesta
    def afinar(self):
        afinacion = random.randint(0, 1)
        if afinacion == 0:
            self._afinado = True
            log.info("El instrumento {} ha sido afinado".format(self.nombre))
            return True
        else:
            self._afinado = False
            log.info("El instrumento {} no se ha afinado".format(self.nombre))
            return False

    @log_orquesta
    def tocar(self):
        if self.afinado:
            return True
        else:
            raise AfinadoException()
