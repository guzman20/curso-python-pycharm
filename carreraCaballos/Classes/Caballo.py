import random

from Classes.Nombrable import Nombrable


class Caballo(Nombrable):
    def __init__(self, id_, nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta, gran_premio):
        Nombrable.__init__(self, id_, nombre)
        self._fecha_nacimiento = fecha_nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        self._gran_premio = gran_premio

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self, valor_apuesta):
        self._valor_apuesta = valor_apuesta

    @property
    def gran_premio(self):
        return self._gran_premio

    @gran_premio.setter
    def gran_premio(self, gran_premio):
        self._gran_premio = gran_premio

    def correr(self):
        return self.velocidad + self.experiencia - edad + random.randint(1, 50)
