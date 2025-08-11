from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    dni = models.CharField(max_length=10)
    legajo =models.CharField(max_length=6, unique=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} | {self.get_full_name()} | {self.get_rol_display()} | DNI: {self.dni} | Legajo: {self.legajo}"
