from django.db import models

class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salario=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.nombre

