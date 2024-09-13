from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    retrive:
    Retorna un Producto Especifico

    list:
    Retorna la lista de todos los Productos

    create:
    Crea un Nuevo Producto

    delete:
    Elimina un Producto

    partial_update:
    Actualiza un producto parcialmente

    update:
    Actualiza un producto completamente
    """
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer

