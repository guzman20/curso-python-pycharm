from Classes.Instrumento import Instrumento


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre, tipo)
        self._num_cuerdas = num_cuerdas

    @property
    def num_cuerdas(self):
        return self._num_cuerdas

    @num_cuerdas.setter
    def num_cuerdas(self, num_cuerdas):
        self._num_cuerdas = num_cuerdas
