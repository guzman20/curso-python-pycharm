from Classes.Guitarra import Guitarra


class Guitarra_Electrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre, tipo, num_cuerdas)
        self.__potencia = potencia

    def get_potencia(self):
        return self.__potencia

    def set_num_potencia(self, potencia):
        self.__potencia = potencia
