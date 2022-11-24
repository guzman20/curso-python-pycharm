from Classes.alumno import Alumno


class Colegio:
    def __init__(self, nombre, lista_alumnos=None):
        if lista_alumnos is None:
            lista_alumnos = {}
        self._nombre = nombre
        self._lista_alumnos = lista_alumnos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def lista_alumnos(self):
        return self._lista_alumnos

    def introducir_alumno(self, dni, alumno):
        self.lista_alumnos()[dni] = alumno

    def to_string(self):
        string = "{} tiene los alumnos: ".format(self.nombre)
        lista_alumnos = list(self._lista_alumnos.values())
        for alumno in lista_alumnos:
            if alumno != lista_alumnos[-1]:
                string += alumno.to_string()+", "
            else:
                string += alumno.to_string()
        return string
