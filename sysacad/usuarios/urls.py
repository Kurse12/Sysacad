from django.urls import path

from usuarios.views import nuevoUsuario



app_name= 'usuarios'

urlpatterns = [
    path('nuevo/', nuevoUsuario, name='nuevo')
]