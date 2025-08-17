from django.urls import path

app_name = 'materias'
from .views import materias
urlpatterns = [
    path('', materias, name='mostrar'),

]