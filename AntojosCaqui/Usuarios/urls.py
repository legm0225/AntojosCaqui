from django.urls import path

from Usuarios.views import vistaPrueba

urlspatterns = [
    path('Prueba', vistaPrueba)
]