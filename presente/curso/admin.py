from django.contrib import admin
from curso.models import Curso, CursoPorAlumno, FechaCursoPorAlumno

class CursoPorAlumnoInLine(admin.TabularInline):
	model = CursoPorAlumno
	extra = 1

class FechaCursoPorAlumnoInline(admin.TabularInline):
	model = FechaCursoPorAlumno
	extra = 1

class CursoAdmin(admin.ModelAdmin):
	inlines=(
		FechaCursoPorAlumnoInline,
	)

admin.site.register(Curso, CursoAdmin)


