from django.shortcuts import render
from .models import Materia
# Create your views here.

def materias(request):
    """
    Vista para mostrar las materias disponibles.
    """
    materias = Materia.objects.all()
    return render(request, 'materias/materias.html', {'materias': materias})
