from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import MovieSerializer

from .models import Movie

#Metodos Seguros

class MovieAllVieSet(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=(AllowAny,)

