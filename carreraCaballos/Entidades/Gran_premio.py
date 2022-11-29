from Entidades.Carrera import Carrera
from Entidades.Nombrable import Nombrable


class Gran_premio(Nombrable):
    def __init__(self, id_, nombre, distancia, num_carreras):
        Nombrable.__init__(self, id_, nombre)
        self._distancia = distancia
        self._num_carreras = num_carreras

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, distancia):
        self._distancia = distancia

    @property
    def num_carreras(self):
        return self._num_carreras

    @num_carreras.setter
    def num_carreras(self, num_carreras):
        self._num_carreras = num_carreras

    def iniciar(self, lista_caballos_general, lista_apostantes):
        contador = 0
        diccionario_apuestas = {}
        lista_caballos = []
        for caballo in lista_caballos_general:
            if caballo.gran_premio == self.id:
                lista_caballos.append(caballo)

        while contador < self.num_carreras:
            for apostante in lista_apostantes:
                apuesta = apostante.apostar(lista_caballos)
                if apuesta is None:
                    pass
                else:
                    diccionario_apuestas[apuesta[0]] = apuesta[1]
            carrera = Carrera(lista_caballos)
            ganador = carrera.iniciar(self.distancia)
            for caballo in lista_caballos:
                if caballo is ganador:
                    caballo.experiencia += 5
                else:
                    caballo.experiencia += 1
            for caballo in diccionario_apuestas.keys():
                if caballo is ganador:
                    lista_apostantes.saldo += diccionario_apuestas[caballo].apuesta * caballo.valor_apuesta
                else:
                    lista_apostantes.saldo -= diccionario_apuestas[caballo].apuesta

        return lista_caballos, lista_apostantes
