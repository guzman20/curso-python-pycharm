import random

from Entidades.Nombrable import Nombrable


class Apostante(Nombrable):
    def __init__(self, id_, nombre, saldo):
        Nombrable.__init__(self, id_, nombre)
        self._saldo = saldo
        self._apuesta = None

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def apuesta(self):
        return self._apuesta

    @apuesta.setter
    def apuesta(self, apuesta):
        self._apuesta = apuesta

    def apostar(self, lista_caballos):
        if self.saldo > 0:
            lista_ids = []
            for caballo in lista_caballos:
                print("Caballo de id {}, de nombre {} y con el valor de apuesta de {}".format(caballo.id,
                                                                                              caballo.nombre,
                                                                                              caballo.valor_apuesta))
                lista_ids.append(caballo.id)
            Error = True
            id_caballo = None
            while Error:
                id_caballo = input("¿A que caballo apuesta?(indiquelo con el id del caballo)")
                if id_caballo in lista_ids:
                    Error = False
                else:
                    print("El caballo de id {} no existe por favor ponga uno correcto".format(id_caballo))
            caballo_seleccionado = None
            for caballo in lista_caballos:
                if caballo.id == id_caballo:
                    caballo_seleccionado = caballo
                    break

            self.apuesta = random.randint(0, self.saldo)
            return caballo_seleccionado, self
        else:
            print("No le queda saldo")
            return None
