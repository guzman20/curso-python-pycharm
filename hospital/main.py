from Clases.Doctor import Doctor
from Clases.Enfermero import Enfermero
from Clases.Habitacion import Habitacion
from Clases.Hospital import Hospital
from Clases.Paciente import Paciente

habitacion_residentes= Habitacion("Habitacion_residentes", 3)
sala_de_espera= Habitacion("Sala_de_espera", 4)
consulta1= Habitacion("Consulta", 2)
consulta2= Habitacion("Consulta", 2)

hospital= Hospital([habitacion_residentes, sala_de_espera, consulta1, consulta2])

doctor1= Doctor("Juan", "neumologia")
doctor2= Doctor("Laura", "cardiologia")
lista_doctores=[doctor1, doctor2]

enfemero1= Enfermero("Jorge", 1)
enfemero2= Enfermero("Maria", 2)
enfemero3= Enfermero("Angel", 3)
lista_enfemeros=[enfemero1, enfemero2, enfemero3]

paciente1= Paciente("Jose", ["Tos", "Graganta Seca"])
paciente2= Paciente("Luisa", ["Dolor en la garganta", "Flemas", "Congestion Nasal"])
paciente3= Paciente("Pedro", ["Diarrea"])
paciente4= Paciente("Pedro", ["Respiracion entre cortada", "Tos"])
lista_pacientes=[paciente1, paciente2, paciente3, paciente4]

hospital.abrir(lista_enfemeros, lista_doctores, lista_pacientes)
hospital.atender()
