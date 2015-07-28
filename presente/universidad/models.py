from django.db import models
from empleados.models import Profesor, Decano, Secretario, Recepcionista, CoordinadorCarrera
# from curso.models import Curso

class Facultad(models.Model):
  decano = models.ForeignKey(Decano)
  secretario = models.ForeignKey(Secretario)
  recepcionista = models.ForeignKey(Recepcionista)
  nombre = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200)
  logo = models.CharField(max_length=200)
  direccion = models.CharField(max_length=200)
  telefono_administracion = models.CharField(max_length=200)
  telefono_alumnado = models.CharField(max_length=200)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return self.nombre+ " -" + self.direccion + "- "


class Carrera(models.Model):
  coordinador = models.ForeignKey(CoordinadorCarrera)	
  facultad = models.ForeignKey(Facultad)
  nombre = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200)
  logo = models.CharField(max_length=200)
  telefono_administracion = models.CharField(max_length=200)
  telefono_alumnado = models.CharField(max_length=200)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return self.nombre

class Semestre(models.Model):
  carrera = models.ForeignKey(Carrera)
  nombre = models.CharField(max_length=200)
  numero = models.IntegerField( )
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return str(self.numero) + " " + self.nombre



class Materia(models.Model):
  profesor_titular = models.ForeignKey(Profesor)
  nombre = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200)
  semestre = models.ForeignKey(Semestre) 
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return self.nombre


# class Planilla(models.Model):
#   curso = models.ForeignKey(Curso)
#   semestre = models.ForeignKey(Semestre)
#   created_at = models.DateField(auto_now_add=True)
#   updated_at = models.DateField(auto_now=True) 

#   def __str__(self):
#     return self.curso