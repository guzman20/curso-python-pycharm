class Alumno:
    def __init__(self, nombre, apellidos, dni, asignaturas=None):
        if asignaturas is None:
            asignaturas = []
        self._nombre = nombre
        self._apellidos = apellidos
        self._dni = dni
        self._asignaturas = asignaturas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    def notas(self):
        return self._asignaturas

    def introducir_asignatura(self, asignatura):
        self._asignaturas.append(asignatura)

    def to_string(self):
        string = "El alumno {} se apellida {}, su dni es {} " \
                 "y esta en las siguientes asignaturas: ".format(self.nombre,
                                                                 self.apellidos,
                                                                 self.dni)
        for asignatura in self._asignaturas:
            string += asignatura + ", "
        return string
