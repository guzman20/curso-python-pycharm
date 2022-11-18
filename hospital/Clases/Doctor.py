import random

from Clases.Enfermo import Enfermo
from Clases.Persona import Persona
from Clases.PersonalHospital import PersonalHospital

# Esta clase es doctor que se encarga de diagnosticar a los pacientes. Hereda de Persona para tener nombre y de
# PersonalHospital para poder fichar


class Doctor(Persona, PersonalHospital):

    # Se apoya en el construtor de persona para introducir el nombre y ademas de sus dos caracteristicas
    # especialidad y enfermedad
    def __init__(self, nombre, especialidad):
        Persona.__init__(self, nombre)
        self.especialidad = especialidad
        self.enfermedades = ["Mononucleosis", "COVID-19", "Gripe", "Gastrointiditis"]

    # Este metodo es para atender a paciente y lo devuelve enfermo o sano
    def atender_paciente(self, paciente):
        # Se genera un numero aleatorio y si es mayor a 7 se devuelve un objeto Enfermo con una enfermedad
        # aleotoria de las lista de enfermedades gracias a la clase random con radint y choice respectivamente
        valoracion = random.randint(0, 10)
        if valoracion > 7:
            return Enfermo(paciente.nombre, random.choice(self.enfermedades))
        else:
            return paciente

    def to_string(self):
        return "{} es doctor y su especialidad es {}".format(super().to_string(), self.especialidad)
