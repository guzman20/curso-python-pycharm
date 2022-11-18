from Clases.Persona import Persona


# La clase paciente es la que crea la gente que visita el hospital y hereda de Persona
class Paciente(Persona):
    # Los pacientes tienen sintomas que se guardan en una lista
    def __init__(self, nombre, sintomas=None):
        Persona.__init__(self, nombre)
        if sintomas is None:
            sintomas = []
        self.sintonmas = sintomas

    # Añade un sintoma a la lista de sintomas
    def add_sintoma(self, sintoma):
        self.personas.append(sintoma)

    # Quita un sintoma de la lista de sintomas
    def remove_sintoma(self, sintoma):
        self.personas.remove(sintoma)

    def to_string(self):
        return "{} es paciente y sus sintomas son {}".format(super().to_string(), self.sintonmas)
