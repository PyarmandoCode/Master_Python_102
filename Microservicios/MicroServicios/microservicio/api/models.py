from django.db import models

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    stock =models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
