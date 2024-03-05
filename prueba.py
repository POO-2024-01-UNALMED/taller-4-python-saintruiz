from classroom.asignatura import Asignatura
from classroom.grupo import Grupo


asignatura1 = Asignatura("Vision por Computador")
asignatura2 = Asignatura("POO", "Salon 503B")

grupo = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])
grupo.listadoAsignaturas(asignatura1="Fundamentos de programacion",
                    asignatura2="Ecuaciones diferenciales",
                    asignatura3="Inteligencia artificial")

print(grupo._asignaturas[0]._nombre) # "Vision por Computador" 
print(grupo._asignaturas[1]._nombre) #"POO" and\
print(grupo._asignaturas[2]._nombre) #"Fundamentos de programacion" and\
print(grupo._asignaturas[3]._nombre) #"Ecuaciones diferenciales" and\
print(grupo._asignaturas[4]._nombre) #"Inteligencia artificial":

