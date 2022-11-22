from Classes.Bar import Bar
from Classes.Camarero import Camarero
from Classes.Cliente import Cliente

if __name__ == '__main__':
    cliente1 = Cliente("Roberto")
    cliente2 = Cliente("Maria")
    cliente3 = Cliente("Alejandro")
    lista_clientes = [cliente1, cliente2, cliente3]

    camarero1 = Camarero("Paco")
    camarero2 = Camarero("Helena")
    lista_camareros = [camarero1, camarero2]

    bar = Bar()

    bar.abrir(lista_camareros)
    bar.atender_clientes(lista_clientes)
