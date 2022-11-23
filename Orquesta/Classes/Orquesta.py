from Classes.Guitarra import Guitarra
from Classes.Guitarra_Electrica import Guitarra_Electrica
from Classes.Piano import Piano
from Classes.Tambor import Tambor
from Exceptions.AfinadoException import AfinadoException
from Utils.Log_orquesta import log


class Orquesta:
    def __init__(self):
        self._lista_instrumentos = []

    def get_lista_instrumentos(self):
        return self._lista_instrumentos

    def crear_orquesta(self):
        guitarra = Guitarra("Española", "guitarra", 10)
        log.info("Guitarra ha sido creada con las caracteristicas {}, {} y {}".format(guitarra.nombre
                                                                                      , guitarra.tipo
                                                                                      , guitarra.num_cuerdas))
        guitarra_electrica = Guitarra_Electrica("Bajo", "electrica", 8, 120)
        log.info("Guitarra electrica ha sido creada con las caracteristicas {}, {}, {} y {}" .format(
                 guitarra_electrica.nombre, guitarra_electrica.tipo, guitarra_electrica.num_cuerdas
                 , guitarra_electrica.potencia))

        piano = Piano("Clasico", "cuerda", 70)
        log.info("Piano ha sido creado con las caracteristicas {}, {} y {}".format(
            piano.nombre, piano.tipo, piano.num_teclas))

        tambor = Tambor("Tamborilete", "piel", "mediano")
        log.info("Tambor ha sido creado con las caracteristicas {}, {} y {}".format(
            tambor.nombre, tambor.tipo, tambor.tamanio))

        self._lista_instrumentos = [guitarra, guitarra_electrica, piano, tambor]

    def iniciar_concierto(self):
        for instrumento in self.get_lista_instrumentos():
            instrumento.afinar()
        for instrumento in self.get_lista_instrumentos():
            try:
                instrumento.tocar()
                log.info("El instrumento {} esta afinado y esta sonando".format(instrumento.nombre))
            except AfinadoException:
                log.error("El instrumento {} no estaba afinado y sono mal".format(instrumento.nombre))
