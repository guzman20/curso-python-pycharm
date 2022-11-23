from Classes.Instrumento import Instrumento
from Exceptions.AfinadoException import AfinadoException
from Utils.Log_orquesta import log

class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre, tipo)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def tocar(self):
        if super(Tambor, self).tocar() is not None:
            self.aporrear()
        else:
            log.error("El instrumento {} no esta afinado y sonó mal".format(self.nombre))
            raise AfinadoException()

    def aporrear(self):
        return "Aporreando el tambor {}".format(self.nombre)
