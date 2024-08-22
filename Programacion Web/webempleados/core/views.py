from django.shortcuts import render
from .models import Empleados

def index(request):
    #select * from empleados
    empleados=Empleados.objects.all()
    context ={
        "empleados":empleados
    }
    return render(request,"index.html",context)

def detalles(request,pk):
    #select * from empleado where id=pk
    empleado=Empleados.objects.get(id=pk)
    context = {
        "empleado":empleado
    }
    return render(request,"detalles.html",context)
