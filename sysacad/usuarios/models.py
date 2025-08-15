from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
import random
from django.db import models


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, dni, first_name, last_name, password=None, rol=None, **extra_fields):
        if not dni:
            raise ValueError("El DNI es obligatorio")
        if rol is None:
            raise ValueError("El rol es obligatorio")

        # Usuario nuevo siempre sin fecha_baja por defecto (activo)
        extra_fields.setdefault('fecha_baja', None)

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

    def create_superuser(self, dni, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('rol', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('fecha_baja', None)

        rol = extra_fields.pop('rol')

        if rol != 'admin':
            raise ValueError('El superusuario debe tener rol admin.')
        if not extra_fields.get('is_staff'):
            raise ValueError('El superusuario debe tener is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(
            dni,
            first_name,
            last_name,
            password=password,
            rol=rol,
            **extra_fields
        )


class Usuario(AbstractUser):
    username = None  # quitamos username para usar dni como identificador único
    dni = models.CharField(max_length=15, unique=True)
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)

    ROL_CHOICES = [
        ("alumno", "Alumno"),
        ("profesor", "Profesor"),
        ("admin", "Administrador"),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    fecha_baja = models.DateField(null=True, blank=True)  # 👈 Nuevo campo

    legajo = models.CharField(max_length=6, unique=True, editable=False)

    USERNAME_FIELD = "legajo"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UsuarioManager()

    @property
    def activo_en_facultad(self):
        return self.fecha_baja is None

    def save(self, *args, **kwargs):
        if not self.legajo:
            while True:
                nuevo_legajo = str(random.randint(100000, 999999))
                if not Usuario.objects.filter(legajo=nuevo_legajo).exists():
                    self.legajo = nuevo_legajo
                    break
        super().save(*args, **kwargs)

    def clean(self):
        # Evitar que un usuario con fecha_baja pueda tener is_active=True
        if self.fecha_baja and self.is_active:
            raise ValidationError("No se puede marcar como activo a un usuario dado de baja.")

    def __str__(self):
        estado = "Activo" if self.activo_en_facultad else f"Baja {self.fecha_baja}"
        return f"{self.first_name} {self.last_name} ({self.rol}) - {estado}"

    def has_perm(self, perm, obj=None):
        # Bloquear permisos si está dado de baja
        if not self.activo_en_facultad:
            return False
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        # Bloquear acceso a módulos si está dado de baja
        if not self.activo_en_facultad:
            return False
        return super().has_module_perms(app_label)
