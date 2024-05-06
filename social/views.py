from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .form import *
from django.contrib.auth import logout


# Create your views here.
def log_out(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
