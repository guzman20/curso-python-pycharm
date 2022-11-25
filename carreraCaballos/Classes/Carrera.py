from Classes.Apuesta import Apuesta


class Carrera:
    def __init__(self, lista_caballos=None):
        if lista_caballos is None:
            lista_caballos = []
        self._lista_caballos = lista_caballos

    @property
    def lista_caballos(self):
        return self._lista_caballos

    @lista_caballos.setter
    def lista_caballos(self, lista_caballos):
        self._lista_caballos = lista_caballos

    def iniciar(self, distancia):
        distancia_recorrida_por_caballo={}
        for caballo in self.lista_caballos:
            distancia_recorrida_por_caballo[caballo] = 0
        while distancia > any(list(distancia_recorrida_por_caballo.values())):

