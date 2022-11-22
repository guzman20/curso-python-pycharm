from Classes.Instrumento import Instrumento


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre, tipo)
        self.__num_teclas = num_teclas

    def get_num_teclas(self):
        return self.__num_teclas

    def set_num_potencia(self, num_teclas):
        self.__num_teclas = num_teclas