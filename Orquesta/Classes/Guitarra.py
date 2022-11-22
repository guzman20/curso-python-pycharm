from Classes.Instrumento import Instrumento


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre, tipo)
        self.__num_cuerdas = num_cuerdas

    def get_num_cuerdas(self):
        return self.__num_cuerdas

    def set_num_cuerdas(self, num_cuerdas):
        self.__num_cuerdas = num_cuerdas
