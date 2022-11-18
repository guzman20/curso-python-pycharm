from Clases.Persona import Persona

# La clase Enfermo es para los pacientes que enferman y hereda de persona
class Enfermo(Persona):
    def __init__(self, nombre, enfermedad):
        Persona.__init__(self, nombre)
        self.enfermedad = enfermedad

    def to_string(self):
        return "{} es enferm@ y su enfermedad es {}".format(super().to_string(), self.enfermedad)
