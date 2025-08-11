from re import U
from django.forms import modelform_factory
from django.shortcuts import redirect, render
from usuarios.models import Usuario

# Create your views here.
UsuarioForm = modelform_factory(Usuario, exclude={})

def nuevoUsuario(request):
    if request.method =='POST':
        formaUsuario = Usuario(request.POST)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('index')
    else:
        formaUsuario = UsuarioForm()
    return render(request, 'usuarios/nuevo.html', {'formaUsuario':formaUsuario})