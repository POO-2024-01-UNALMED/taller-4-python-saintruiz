from classroom.asignatura import Asignatura

class Grupo:
    grado = 12

    def __init__(self, grupo="grupo determinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **args):
        if self._asignaturas==None:
            self._asignaturas=[]
        for x in args.values():
            self._asignaturas.append(x)

    def agregarAlumno(self, alumno, lista=None):
        if lista==None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos=lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 10"):
    #     cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre
