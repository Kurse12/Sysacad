
from webbrowser import get
from django.forms import modelform_factory
from django.shortcuts import redirect, render
from django.urls import reverse
from usuarios.forms import CustomAuthenticationForm
from usuarios.models import Usuario
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Create your views here.



def login(request):
    return render(request, 'login.html' )

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True  # Usuarios logueados van directo a su dashboard

    def form_valid(self, form):
        # Expira la sesión al cerrar navegador
        self.request.session.set_expiry(0)
        return super().form_valid(form)

    def get_success_url(self):
        user = self.request.user

        if user.rol == 'alumno':
            return reverse('webapp:menuAlumno')
        elif user.rol == 'profesor':
            return reverse('webapp:menuProfesor')
        else:
            # Desloguea cualquier usuario con rol no permitido y redirige al login
            logout(self.request)
            return reverse('usuarios:login')
        
