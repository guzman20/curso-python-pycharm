# La clase de la cual muchas heredan para poder tener nombre y es comun a todas las personas
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def to_string(self):
        return "La persona se llama {}".format(self.nombre)
