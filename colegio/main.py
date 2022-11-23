from Classes.alumno import Alumno
from Classes.colegio import Colegio

if __name__ == '__main__':
    try:
        archivo = open('alumnos-colegio.txt', 'r')
        colegios = {}
        for linea in archivo:
            palabras = linea.split("|")
            colegio = palabras[0]
            if colegio in colegios.keys():
                colegioSeleccionado = colegios[colegio]
                alumno = Alumno(palabras[1], palabras[2], palabras[3])
                asignaturas = palabras[4].split(";")
                for asignatura in asignaturas:
                    alumno.introducir_asignatura(asignatura)
                colegioSeleccionado.introducir_alumno(alumno.dni, alumno)
                colegios[colegioSeleccionado.nombre] = colegioSeleccionado
            else:
                colegios[colegio] = Colegio(colegio)
                colegioSeleccionado = colegios[colegio]
                alumno = Alumno(palabras[1], palabras[2], palabras[3])
                asignaturas = palabras[4].split(";")
                for asignatura in asignaturas:
                    alumno.introducir_asignatura(asignatura)
                colegioSeleccionado.introducir_alumno(alumno.dni, alumno)
                colegios[colegioSeleccionado.nombre] = colegioSeleccionado
        for colegio in colegios.values():
            print(colegio.to_string())
    except IOError:
        print("Error")
    finally:
        archivo.close()
