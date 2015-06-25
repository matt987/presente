from django.db import models

class Alumno(models.Model):
  nombre = models.CharField(max_length=200)
  apellido = models.CharField(max_length=200)
  ci = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  direccion = models.CharField(max_length=200)
  telefono = models.CharField(max_length=200)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return self.apellido + ", " + self.nombre


  
