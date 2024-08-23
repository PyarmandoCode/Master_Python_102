from django.urls import path
from . import views

#Son los ENDPOINTS
urlpatterns = [
    path('api/List_All_Movies', views.MovieAllVieSet.as_view()),
]
