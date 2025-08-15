from django.urls import path

from django.contrib.auth import views as auth_views

from usuarios.views import CustomLoginView



app_name= 'usuarios'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    
]