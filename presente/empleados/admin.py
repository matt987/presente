from django.contrib import admin
from empleados.models import Empleado, Profesor, Decano, Secretario, Recepcionista, CoordinadorCarrera

admin.site.register(Empleado)

admin.site.register(Profesor)
admin.site.register(Decano)
admin.site.register(Secretario)
admin.site.register(Recepcionista)
admin.site.register(CoordinadorCarrera)
# Register your models here.
