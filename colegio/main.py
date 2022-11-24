from Classes.alumno import Alumno
from Classes.colegio import Colegio

if __name__ == '__main__':
    try:
        # leemos el archivo y creamos un diccionario para los colegios
        archivo = open('alumnos-colegio.txt', 'r')
        colegios = {}
        # Recorremos las lineas del archivo txt
        for linea in archivo:
            # Dividimos la lineas por las | que separan los elementos
            palabras = linea.split("|")
            # Sacamos el nombre del colegio
            colegio = palabras[0]
            # Si el colegio ya se encuentra entre las claves del diccionario solo hay que añadir al alumno
            if colegio in colegios.keys():
                # Extraemos el colegio
                colegioSeleccionado = colegios[colegio]
                # Creamos el alumno a partir de la informacion que nos dan
                alumno = Alumno(palabras[1], palabras[2], palabras[3])
                asignaturas = palabras[4].split(";")
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
                alumno = Alumno(palabras[1], palabras[2], palabras[3])
                asignaturas = palabras[4].split(";")
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
