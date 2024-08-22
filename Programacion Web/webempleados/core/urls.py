from django.urls import path
from .views import index,detalles

urlpatterns = [
    path('', index),
    path('detalles/<int:pk>',detalles,name="detalles")
]
