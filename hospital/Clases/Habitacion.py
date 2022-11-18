# La clase habitacion es para definir las habitaciones del hospital en este caso
class Habitacion:
    # Las habitaciones tiene un tipo que se refiere para que son y una capacidad
    # que es el numero maximo de personas que pueden haber al mismo tiempo ademas de una lista de estos
    def __init__(self, tipo, capacidad):
        self.capacidad = capacidad
        self.personas = []
        self.tipo = tipo

    # Añade una persona a la lista de personas
    def add_persona(self, persona):
        self.personas.append(persona)

    # Borra una persona de la lista de personas
    def remove_persona(self, persona):
        self.personas.remove(persona)

    # Verifica si la habitacion esta vacia es decir que la lista personas no tenga elementos
    def is_empty(self):
        if len(self.personas) == 0:
            return True
        else:
            return False

    # Verifica si la habitacion esta llena es decir que la lista de personas tenga la misma longitud que la capacidad
    def is_full(self):
        if len(self.personas) == self.capacidad:
            return True
        else:
            return False

    def to_string(self):
        personas = list(map(lambda persona: persona.to_string(), self.personas))
        return "La habitacion es {}, tiene una capacidad de {} y tiene estas personas :{}\n".format(self.tipo,
                                                                                                    self.capacidad,
                                                                                                    personas)
