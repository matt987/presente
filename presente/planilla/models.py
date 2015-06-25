from django.db import models
from empleados.models import Profesor
from curso.models import Curso, CursoPorAlumno
from universidad.models import Semestre


class Planilla(models.Model):
  curso = models.ForeignKey(Curso)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
  	return str(self.curso)