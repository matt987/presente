from django.contrib import admin
from curso.models import Curso, CursoPorAlumno

class CursoPorAlumnoInLine(admin.TabularInline):
	model = CursoPorAlumno
	extra = 10

class CursoAdmin(admin.ModelAdmin):
	inlines=(
		CursoPorAlumnoInLine,
	)

admin.site.register(Curso, CursoAdmin)

