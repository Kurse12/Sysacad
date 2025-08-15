from django.http import HttpResponseForbidden

def rol_required(roles):
    # 'roles' es la lista de roles permitidos para esa vista
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                # Si no está logueado, bloquea el acceso
                return HttpResponseForbidden("No autenticado")
            if request.user.rol not in roles:
                # Si no tiene un rol permitido, bloquea el acceso
                return HttpResponseForbidden("No autorizado")
            # Si pasa las verificaciones, ejecuta la vista original
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator