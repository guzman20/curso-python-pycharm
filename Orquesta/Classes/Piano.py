from Classes.Instrumento import Instrumento


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre, tipo)
        self._num_teclas = num_teclas

    @property
    def num_teclas(self):
        return self._num_teclas

    @num_teclas.setter
    def num_teclas(self, num_teclas):
        self._num_teclas = num_teclas
