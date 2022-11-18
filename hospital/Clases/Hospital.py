from Clases.Doctor import Doctor
from Clases.Enfermo import Enfermo
from Clases.Paciente import Paciente


# La clase hospital contiene a todas las demas y se compone de ellas
class Hospital:
    # En el constructor solo pediremos las habitaciones si ya están creadas, pero se puede hacer sin nada
    def __init__(self, habitaciones=None):
        if habitaciones is None:
            habitaciones = []
        self.habitaciones = habitaciones

    # Añade una habitacion a la lista de habitaciones
    def add_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Quitar una habitacion de la lista de habitaciones
    def remove_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)

    # Inicia una simulacion de un dia y, por tanto, se pide los enfermeros, doctores y pacientes
    def abrir(self, enfermeros, doctores, pacientes):
        # Primero fichamos a los enfermeros
        for enfermero in enfermeros:
            enfermero.fichar()
        # Después fichamos a los doctores y les colocamos en las consultas
        for doctor in doctores:
            doctor.fichar()
            # Con un for verificando de que habitaciones y si están vaciás
            for habitacion in self.habitaciones:
                # Si se encuentran se pone a un doctor en cada consulta y se cierra con break
                if habitacion.tipo == "Consulta" and habitacion.is_empty():
                    habitacion.add_persona(doctor)
                    self.habitaciones[self.habitaciones.index(habitacion)] = habitacion
                    print("El doctor " + doctor.nombre + " esta en la consulta.")
                    break
        # Encontramos la sala de espera y la llenamos de pacientes
        habitacion_espera = None
        for habitacion in self.habitaciones:
            if habitacion.tipo == "Sala_de_espera":
                habitacion_espera = habitacion
                break
        for paciente in pacientes:
            habitacion_espera.add_persona(paciente)
        self.habitaciones[self.habitaciones.index(habitacion_espera)] = habitacion_espera

    # Esta funcion sirve para simular cuando comienza a atenderse a los pacientes
    def atender(self):
        # Primero localizamos las salas y las guardamos en una variable auxiliar
        habitacion_espera = None
        consultas = []
        habitacion_residentes = None
        doctor = None
        paciente = None
        for habitacion in self.habitaciones:
            if habitacion.tipo == "Sala_de_espera":
                habitacion_espera = habitacion
            elif habitacion.tipo == "Consulta":
                consultas.append(habitacion)
            elif habitacion.tipo == "Habitacion_residentes":
                habitacion_residentes = habitacion
        # Un bucle que se repite hasta que no queden pacientes
        while not habitacion_espera.is_empty():
            # Llenamos las consultas de pacientes
            for habitacion in consultas:
                if any(type(persona) is Doctor for persona in habitacion.personas) and not habitacion.is_full():
                    paciente = habitacion_espera.personas.pop(0)
                    self.habitaciones[self.habitaciones.index(habitacion_espera)] = habitacion_espera
                    habitacion.add_persona(paciente)
                    self.habitaciones[self.habitaciones.index(habitacion)] = habitacion
            # Recorremos las consultas y verificamos y guardamos los doctores y pacientes
            for habitacion in consultas:
                for persona in habitacion.personas:
                    if type(persona) is Doctor:
                        doctor = persona
                    elif type(persona) is Paciente:
                        paciente = persona
                # Si hay pacientes se diagnostican a los pacientes
                if paciente is not None:
                    paciente = doctor.atender_paciente(paciente)
                    # Dependiendo del resultado si es sano se manda a casa
                    if type(paciente) is not Enfermo:
                        # Se usa una lista auxiliar para quitar el paciente de la consulta y se sobreescribe
                        lista_aux = habitacion
                        lista_aux.personas.pop(1)
                        self.habitaciones[self.habitaciones.index(habitacion)] = lista_aux
                        print("El paciente {} no esta enfermo puede ir a su casa".format(
                            paciente.nombre))
                    # Si está enfermo y queda hueco en las habitaciones se hospitaliza
                    elif type(paciente) is Enfermo and not habitacion_residentes.is_full():
                        # Se usa una lista auxiliar para quitar al paciente de la consulta se guarda el paciente y se
                        # lleva la habitacion de residentes
                        lista_aux = habitacion
                        enfermo = lista_aux.personas.pop(1)
                        self.habitaciones[self.habitaciones.index(habitacion)] = lista_aux
                        habitacion_residentes.add_persona(enfermo)
                        self.habitaciones[self.habitaciones.index(habitacion_residentes)] = habitacion_residentes
                        print("El paciente {} esta enfermo y ha sido hospitalizado".format(
                            paciente.nombre))
                    # Si está enfermo, pero están llenas las habitaciones se deriva a otro hospital
                    elif type(paciente) is Enfermo and habitacion_residentes.is_full():
                        # Se usa una lista auxiliar para quitar el paciente de la consulta y se sobreescribe
                        lista_aux = habitacion
                        lista_aux.personas.pop(1)
                        self.habitaciones[self.habitaciones.index(habitacion)] = lista_aux
                        print("El paciente {} que esta enfermo no puede ser atendido se llevara a otro hospital".format(
                            paciente.nombre))

    def to_string(self):
        habitaciones = list(map(lambda habitacion: habitacion.to_string(), self.habitaciones))
        return "El hospital tiene estas habitaciones :{}\n".format(habitaciones)
