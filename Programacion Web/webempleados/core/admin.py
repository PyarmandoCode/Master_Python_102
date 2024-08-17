from django.contrib import admin
from .models import Empleados,Pasaporte,Direcciones,Curso

admin.site.register([Empleados,Pasaporte,Direcciones,Curso])


