from django.shortcuts import render
from .models import Empleados

def index(request):
    empleados=Empleados.objects.all()
    context ={
        "empleados":empleados
    }
    return render(request,"index.html",context)
