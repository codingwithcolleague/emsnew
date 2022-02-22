from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request,*args,**kwargs):
            if request.role in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return redirect("employee:list")
        return wrap
    return decorator


def admin_only(view_func):
    def wrap(request,*args,**kwargs):
        if request.role == 'Admin':
            return view_func(request,*args,**kwargs)
        else:
            return redirect("employee:list")
    return wrap