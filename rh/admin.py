from django.contrib import admin

from rh.models import Departamento, Funcionario

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Departamento)