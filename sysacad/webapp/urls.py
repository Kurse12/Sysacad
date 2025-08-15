from .views import  menuAlumno
from django.contrib.auth import views as auth_views
from django.urls import path



app_name = 'webapp'

urlpatterns = [
    path('menuAlumno/', menuAlumno, name='menuAlumno'),
    
]