from classroom.asignatura import *
from classroom.grupo import *

asignatura1 = Asignatura("Vision por Computador")
asignatura2 = Asignatura("POO", "Salon 503B")

grupo1 = Grupo()
grupo2 = Grupo("Grupo 32")
grupo3 = Grupo("Grupo 23", [asignatura1])
grupo4 = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])

print(grupo1._grupo) 
print(grupo1._asignaturas)
print(grupo1.listadoAlumnos)
print(grupo2._grupo)
print(grupo2._asignaturas)
print(grupo2.listadoAlumnos)
print(grupo3._grupo)
print(grupo3._asignaturas)
print(grupo3.listadoAlumnos)
print(grupo4._grupo)
print(grupo4._asignaturas)
print(grupo4.listadoAlumnos) 
print(Grupo.grado)