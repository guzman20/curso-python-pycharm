from Classes.Guitarra import Guitarra


class Guitarra_Electrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre, tipo, num_cuerdas)
        self._potencia = potencia

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia
