from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from .form import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DeleteView
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity
from django.contrib.auth.decorators import login_required


# Create your views here.
def log_out(request):
    logout(request)
    return HttpResponse('you has exited')


def index(request):
    return HttpResponse('you has entered')


def profile(request):
    return HttpResponse('you has entered')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_account(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user, files=request.FILES)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = EditUserForm(instance=request.user)
    context = {
        'user_form': user_form
    }

    return render(request, 'registration/edit_account.html', {'user_form': user_form, 'context': context})
