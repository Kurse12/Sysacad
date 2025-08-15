from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

user = get_user_model()

def menuAlumno(request):
    return render(request, 'webapp/menuAlumno.html', {
        'usuario': obtener_usuario(request)
    })

def obtener_usuario(request):
    if request.user.is_authenticated:
        try:
            usuario = user.objects.get(first_name=request.user.first_name, last_name=request.user.last_name)
            return usuario
        except user.DoesNotExist:
            return None
    return None