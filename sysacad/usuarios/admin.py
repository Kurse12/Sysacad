from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario

    fieldsets = (
        (None, {"fields": ("dni", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "rol", "legajo")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("dni", "first_name", "last_name", "rol", "password1", "password2"),
        }),
    )

    list_display = ("dni", "first_name", "last_name", "rol", "legajo", "is_staff")
    readonly_fields = ("legajo",)

    search_fields = ("dni", "first_name", "last_name")
    ordering = ("dni",)
