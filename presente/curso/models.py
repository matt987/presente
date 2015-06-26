from django.db import models
from alumnos.models import Alumno
from universidad.models import Materia

class Curso(models.Model):
  materia = models.ForeignKey(Materia)
  anio = models.IntegerField(default=2015) 
  descripcion = models.CharField(max_length=200,default="")
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  def __str__(self):
    return str(self.materia) + " - " + str(self.anio)

class CursoPorAlumno(models.Model):
  curso = models.ForeignKey(Curso)
  alumno = models.ForeignKey(Alumno)  
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)  
  def __str__(self):
    return "# " + str(self.id) + " " + str(self.alumno)

class FechaCursoPorAlumno(models.Model):
  curso_por_alumno = models.ForeignKey(CursoPorAlumno)
  curso = models.ForeignKey(Curso)
  fecha = models.DateField();
  asistencia = models.BooleanField(default=False)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  def __str__(self):
    return "# " + str(self.id)  

  # timestamp