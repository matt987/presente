from django.db import models

class Empleado(models.Model):
  nombre = models.CharField(max_length=200)
  apellido = models.CharField(max_length=200)
  ci = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  direccion = models.CharField(max_length=200)
  telefono = models.CharField(max_length=200)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 

  def __str__(self):
    return self.apellido + ", " + self.nombre + "(" + self.ci + ")"


class Profesor(models.Model):
	empleado = models.ForeignKey(Empleado)
	def __str__(self):
		return str(self.empleado)

class Decano(models.Model):
	empleado = models.ForeignKey(Empleado)
	def __str__(self):
		return str(self.empleado)

class Secretario(models.Model):
	empleado = models.ForeignKey(Empleado)	
	def __str__(self):
		return str(self.empleado)

class Recepcionista(models.Model):
	empleado = models.ForeignKey(Empleado)	
	def __str__(self):
		return str(self.empleado)

class CoordinadorCarrera(models.Model):
	empleado = models.ForeignKey(Empleado)	
	def __str__(self):
		return str(self.empleado)
