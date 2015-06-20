from django.contrib import admin
from alumnos.models import Alumno
from curso.models import Curso, CursoPorAlumno

class CursoPorAlumnoInLine(admin.TabularInline):
	model = CursoPorAlumno
	extra = 1

class AlumnoAdmin(admin.ModelAdmin):
	inlines=(
		CursoPorAlumnoInLine,
	)

admin.site.register(Alumno, AlumnoAdmin)