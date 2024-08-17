from django.db import models

class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salario=models.DecimalField(max_digits=10,decimal_places=2)
    cargo=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.nombre

class Pasaporte(models.Model):
    empleado=models.OneToOneField(Empleados,on_delete=models.CASCADE)
    pasaporte_numero=models.CharField(max_length=50)


class Direcciones(models.Model):
    empleado=models.ForeignKey(Empleados,on_delete=models.CASCADE)
    direccion=models.CharField(max_length=100)

    def __str__(self):
        return self.direccion
    
 #En este ejemplo un empleado puede tener muchas direcciones pero cada direccion solo pertenece a un empleado   

class Curso(models.Model):
    nombre=models.CharField(max_length=200)
    empleados=models.ManyToManyField(Empleados)

    
