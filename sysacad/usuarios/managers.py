# usuarios/managers.py
from django.contrib.auth.base_user import BaseUserManager

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, dni, first_name, last_name, rol, password=None, **extra_fields):
        if not dni:
            raise ValueError("El DNI es obligatorio")
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

    def create_superuser(self, dni, first_name, last_name, rol="admin", password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(dni, first_name, last_name, rol, password, **extra_fields)
