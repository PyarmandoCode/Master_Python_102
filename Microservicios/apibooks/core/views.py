#Esta Clase me permite crear un servicio restfull pre-creado
#Rest-Full=get-post-put-delete
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
     queryset=Student.objects.all()
     serializer_class=StudentSerializer


