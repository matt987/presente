from django.db import models
from alumnos.models import Alumno
from universidad.models import Materia

class Curso(models.Model):
  materia = models.ForeignKey(Materia)
  descripcion = models.CharField(max_length=200,default="")
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  def __str__(self):
    return str(self.descripcion)

class CursoPorAlumno(models.Model):
  curso = models.ForeignKey(Curso)
  alumno = models.ForeignKey(Alumno)