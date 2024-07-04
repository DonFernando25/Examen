from django.shortcuts import redirect
from functools import wraps

def admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if 'admin_id' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('IniAd')
    return wrap


def usuario_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if 'usuario_rut' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('IniSe')
    return wrap