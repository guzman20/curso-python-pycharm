from Clases.Persona import Persona
from Clases.PersonalHospital import PersonalHospital


# Clase para generar enfermeros que hereda de Persona y PersonalHospital
class Enfermero(Persona, PersonalHospital):
    def __init__(self, nombre, planta):
        Persona.__init__(self, nombre)
        self.planta = planta

    # Se sobreescribe la clase fichar para decir en que planta se situa el enfermero cuando ficha
    def fichar(self):
        super().fichar()
        print("El enfermer@ {} ya esta en la planta {}".format(self.nombre, self.planta))

    def to_string(self):
        return "{} es enfermer@ y su planta es {}".format(super().to_string(), self.planta)
