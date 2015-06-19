from django.db import models
from alumnos.models import Alumno
from universidad.models import Materia

class Planilla(models.Model):
	materia = models.ForeignKey(Materia)
	fecha = models.DateField()
	created_at = models.DateField(auto_now_add=True)
  	updated_at = models.DateField(auto_now=True)
	def __str__(self):
		return str(self.fecha)

class PlanillaPorAlumno(models.Model):
	planilla = models.ForeignKey(Planilla)
	alumno = models.ForeignKey(Alumno)
	asistencia = models.BooleanField(default=True)

