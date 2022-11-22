from Classes.Instrumento import Instrumento


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre, tipo)
        self.__tamanio = tamanio

    def get_tamanio(self):
        return self.__tamanio

    def set_tamanio(self, tamanio):
        self.__tamanio = tamanio

    def tocar(self):
        if super(Tambor, self).tocar() is not None:
            self.aporrear()
        else:
            pass

    def aporrear(self):
        return "Aporreando el tambor {}".format(self._nombre)
