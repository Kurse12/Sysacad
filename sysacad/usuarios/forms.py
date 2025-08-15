from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Legajo")

    def confirm_login_allowed(self, user):
        if hasattr(user, 'fecha_baja') and user.fecha_baja:
            raise forms.ValidationError(
                "Este usuario está dado de baja.",
                code='inactive',
            )
