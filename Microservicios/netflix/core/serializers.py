from rest_framework import serializers
from .models import Movie

#Proporciones un Api Rest para acceder a peliculas y modelos de personas

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['title','sipnosis','release_year','language','genre','top']