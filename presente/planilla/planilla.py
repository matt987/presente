from django.db import models
from empleados.models import Profesor, Decano, Secretario, Recepcionista, CoordinadorCarrera
from curso.models import Curso, CursoPorAlumno


class Planilla(models.Model):
  curso = models.ForeignKey(Curso)
  semestre = models.ForeignKey(Semestre)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return self.curso