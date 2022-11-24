from Classes.alumno import Alumno
from Classes.colegio import Colegio

# Parametros de lectura del fichero
COLEGIO = 0
ALUMNO_NOMBRE = 1
ALUMNO_APELLIDOS = 2
ALUMNO_DNI = 3
ALUMNO_ASIGNATURAS = 4
SEPARADOR_ALUMNOS = "|"
SEPARADOR_ASIGNATURAS = ";"


if __name__ == '__main__':
    colegios = {}
    try:
        # leemos el archivo y creamos un diccionario para los colegios
        archivo = open('alumnos-colegio.txt', 'r')
        # Recorremos las lineas del archivo txt
        for linea in archivo:
            # Dividimos la lineas por las | que separan los elementos
            palabras = linea.split(SEPARADOR_ALUMNOS)
            # Sacamos el nombre del colegio
            colegio = palabras[COLEGIO]
            # Si el colegio ya se encuentra entre las claves del diccionario solo hay que añadir al alumno
            if colegio in colegios.keys():
                # Extraemos el colegio
                colegioSeleccionado = colegios[colegio]
                # Creamos el alumno a partir de la informacion que nos dan
                alumno = Alumno(palabras[ALUMNO_NOMBRE], palabras[ALUMNO_APELLIDOS], palabras[ALUMNO_DNI])
                asignaturas = palabras[ALUMNO_ASIGNATURAS].split(SEPARADOR_ASIGNATURAS)
                for asignatura in asignaturas:
                    alumno.introducir_asignatura(asignatura)
                # Añadimos el alumno al colegio con la clave de su dni
                colegioSeleccionado.introducir_alumno(alumno.dni, alumno)
                # Actualizamos el colegio del diccionario de colegios
                colegios[colegioSeleccionado.nombre] = colegioSeleccionado
            # En el caso de ser el primer alumno en ser añadido se crea el objeto colegio en colegios
            else:
                # Se crea el colegio con el nombre que nos dan y se añade a la array
                colegios[colegio] = Colegio(colegio)
                colegioSeleccionado = colegios[colegio]
                # El resto es como antes
                alumno = Alumno(palabras[ALUMNO_NOMBRE], palabras[ALUMNO_APELLIDOS], palabras[ALUMNO_DNI])
                asignaturas = palabras[ALUMNO_ASIGNATURAS].split(SEPARADOR_ASIGNATURAS)
                for asignatura in asignaturas:
                    alumno.introducir_asignatura(asignatura)
                colegioSeleccionado.introducir_alumno(alumno.dni, alumno)
                colegios[colegioSeleccionado.nombre] = colegioSeleccionado
        # Imprimimos los colegios para verificar que se han añadido bien
        for colegio in colegios.values():
            print(colegio.to_string())
    except IOError:
        print("Error")
    finally:
        # Importante cerramos el archivo incluso si da error de lectura
        archivo.close()
    try:
        # Creamos el archivo de escritura
        archivo = open("prueba2.txt", 'w')
        # Recorremos los colegios
        for colegio in colegios.values():
            # Por alumno
            for alumno in colegio.lista_alumnos().values():
                # Creamos la linea del alumno con su informacion dividida por tuberias
                string = colegio.nombre + SEPARADOR_ALUMNOS + alumno.nombre + SEPARADOR_ALUMNOS + alumno.apellidos + SEPARADOR_ALUMNOS + alumno.dni + SEPARADOR_ALUMNOS
                # Hacemos la lista de asignaturas divididas por el punto y coma
                for asignatura in alumno.notas():
                    if alumno.notas()[-1] != asignatura:
                        string = string + asignatura + SEPARADOR_ASIGNATURAS
                    else:
                        string = string + asignatura
                # Ecribimos la linea ,es decir, el alumno
                archivo.write(string)
    except IOError:
        print("Error")
    finally:
        # Importante cerramos el archivo incluso si da error de lectura
        archivo.close()

