import random

from Classes.Persona import Persona
from Classes.TazaCafe import TazaCafe


class Camarero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def servir_cafe(self, tipo_cafe):
        return TazaCafe(tipo_cafe, random.randint(0, 100))

    def pedir_cafe(self, cliente):
        return self.servir_cafe(input("Que cafe quiere señor/señorita {}".format(cliente.nombre)))
