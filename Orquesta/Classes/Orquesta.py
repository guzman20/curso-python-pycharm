from Classes.Guitarra import Guitarra
from Classes.Guitarra_Electrica import Guitarra_Electrica
from Classes.Piano import Piano
from Classes.Tambor import Tambor
from Utils.Log_orquesta import log


class Orquesta:
    def __init__(self):
        self._lista_instrumentos = []

    def crear_orquesta(self):
        guitarra = Guitarra("Española", "guitarra", 10)
        log.info("Guitarra ha sido creada con las caracteristicas {}, {} y {}".format(guitarra.get_nombre(), guitarra.get, guitarra._num_cuerdas))
        guitarra_electrica = Guitarra_Electrica("Bajo", "electrica", 8, 120)
        piano = Piano("Clasico", "cuerda", 70)
        tambor = Tambor("Tamborilete", "piel", "mediano")
        self._lista_instrumentos = [guitarra, guitarra_electrica, piano, tambor]
