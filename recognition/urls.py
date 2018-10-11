
from django.urls import path
from . import views

urlpatterns = [
    path('detecta_faces', views.detecta_faces, name="detecta_faces"),
    path('detecta_objetos', views.detecta_objetos, name="detecta_objetos"),
]
