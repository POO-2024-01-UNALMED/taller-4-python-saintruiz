from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    asignatura1 = Asignatura("Matematicas")
    asignatura2 = Asignatura("Castellano", "Salon 201")
    grupo1 = Grupo()

    print(asignatura1)
    print(grupo1)
    print(grupo1.grado)

    grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])
    #Grupo 5, Asignaturas=[], listadoAlumnos=[Alejandro, Carlos], grado 12
    grupo3 = Grupo()
    #Grupo determinado, Asig=[], listadoAlumnos=[], grado 12
    grupo4 = Grupo()
    #Grupo determinado, Asignaturas=[], listadoAlumnos=[], grado 12
    grupo5 = Grupo()
    #Grupo determinado, Asignaturas=[], listadoAlumnos=[], grado 12

    grupo3.agregarAlumno("Kelly")
    #Grupo determinado, Asignaturas=[], listadoAlumnos=["Kelly"], grado 12

    grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"])
    #Grupo determinado, Asignaturas=[], listadoAlumnos=["Jaime", "Pedro", "Santiago"], grado 12

    grupo5.agregarAlumno("Javier")
    #Grupo determinado, Asignaturas=[], listadoAlumnos=["Javier"], grado 12

    print(grupo3.listadoAlumnos)
    print(grupo4.listadoAlumnos)
    print(grupo5.listadoAlumnos)

    grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles")
    #Grupo determinado, Asignaturas=["Ciencias", "Quimica", "Ingles"], listadoAlumnos=["Kelly"], grado 12

    print(len(grupo3._asignaturas))

    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)
    Grupo.asignarNombre()
    print(Grupo.grado)



