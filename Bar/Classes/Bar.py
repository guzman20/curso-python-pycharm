import random

from Exceptions.TooColdTemperatureException import TooColdTemperatureException
from Exceptions.TooHotTemperatureException import TooHotTemperatureException


class Bar:
    def __init__(self, lista_clientes=None, lista_camareros=None):
        if lista_camareros is None:
            lista_camareros = []
        if lista_clientes is None:
            lista_clientes = []
        self.lista_clientes = lista_clientes
        self.lista_camareros = lista_camareros

    # Introducimos, si es necesario, camareros nuevos a la lista de camareros
    def abrir(self, lista_camareros):
        if lista_camareros is not None and len(lista_camareros) > 0:
            for camarero in lista_camareros:
                self.lista_camareros.append(camarero)

    # Introducimos, si es necesario, clientes nuevos a la lista de clientes
    def atender_clientes(self, lista_clientes):
        taza = None
        camarero = None
        contador = 0
        if lista_clientes is not None and len(lista_clientes) > 0:
            for cliente in lista_clientes:
                self.lista_clientes.append(cliente)
        while len(self.lista_clientes) > 0:
            try:
                cliente = self.lista_clientes.pop()
                camarero = self.lista_camareros[contador % len(self.lista_camareros)]
                contador += 1
                taza = camarero.servir_cafe(input("Que cafe quiere señor/señorita {} ".format(cliente.nombre)))
                cliente.tomar_taza_cafe(taza)
                print("El cliente {} ha pedido {} al camarero {} ".format(cliente.nombre, taza.tipo_cafe,
                                                                          camarero.nombre))
            except TooHotTemperatureException:
                print("El cliente {} se ha quemado con un {} del camarero {} ".format(cliente.nombre, taza.tipo_cafe,
                                                                                      camarero.nombre))
            except TooColdTemperatureException:
                print("El cliente {} tiene frio el {} del camarero {} ".format(cliente.nombre, taza.tipo_cafe,
                                                                               camarero.nombre))
