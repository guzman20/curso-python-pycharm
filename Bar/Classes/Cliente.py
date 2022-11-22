from Classes.Persona import Persona
from Exceptions.TooColdTemperatureException import TooColdTemperatureException
from Exceptions.TooHotTemperatureException import TooHotTemperatureException


class Cliente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tomar_taza_cafe(self, taza_cafe):
        if taza_cafe.temperatura > 80:
            raise TooHotTemperatureException()
        elif taza_cafe.temperatura < 20:
            raise TooColdTemperatureException()
        else:
            return True
