from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
import random

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, dni, first_name, last_name, password=None, rol=None, **extra_fields):
        if not dni:
            raise ValueError("El DNI es obligatorio")
        if not first_name:
            raise ValueError("El nombre es obligatorio")
        if not last_name:
            raise ValueError("El apellido es obligatorio")
        if rol is None:
            raise ValueError("El rol es obligatorio")

        extra_fields.setdefault('fecha_baja', None)

        # Si no hay legajo, se genera automáticamente
        if 'legajo' not in extra_fields:
            while True:
                nuevo_legajo = str(random.randint(100000, 999999))
                if not Usuario.objects.filter(legajo=nuevo_legajo).exists():
                    extra_fields['legajo'] = nuevo_legajo
                    break

        user = self.model(
            dni=dni,
            first_name=first_name,
            last_name=last_name,
            rol=rol,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, first_name, last_name, password=None, **extra_fields):
        # Campos obligatorios para superuser
        extra_fields.setdefault('rol', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('fecha_baja', None)
        extra_fields.setdefault('legajo', None)  # superuser no tiene legajo

        rol = extra_fields.pop('rol')

        return self.create_user(
            dni=dni,
            first_name=first_name,
            last_name=last_name,
            password=password,
            rol=rol,
            **extra_fields
        )


class Usuario(AbstractUser):
    username = None  # eliminamos username
    dni = models.CharField(max_length=15, unique=True)
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)

    ROL_CHOICES = [
        ("alumno", "Alumno"),
        ("profesor", "Profesor"),
        ("admin", "Administrador"),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    fecha_baja = models.DateField(null=True, blank=True)
    legajo = models.CharField(max_length=6, unique=True, editable=False, null=True, blank=True)# para superuser permitido nulo

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UsuarioManager()

    @property
    def activo_en_facultad(self):
        return self
