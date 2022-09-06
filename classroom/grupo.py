from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def __str__(self):
        return "Grupo de estudiantes: grupo predeterminado"

    def listadoAsignaturas(self, **kwargs):
        
        if(self._asignaturas is None):
            self._asignaturas=[]
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            lista=[]
        else:
            self.listadoAlumnos=[alumno]
        lista.append(alumno)
        self.listadoAlumnos = lista
        

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
