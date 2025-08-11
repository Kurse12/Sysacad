"""
URL configuration for sysacad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from webapp.views import bienvenido
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('usuarios/', include(('usuarios.urls','usuarios'), namespace='usuarios')),
    path('materias/', include(('materias.urls','materias'), namespace='materias')),
    path('inscripciones/', include(('inscripciones.urls','inscripciones'), namespace='inscripciones')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)