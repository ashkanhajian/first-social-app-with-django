from django.db.models import Count
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
from django.core.mail import send_mail
from .models import *
from taggit.models import Tag


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


def ticket(request):
    send = False

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            messge = f"{cd["name"]}\n{cd["email"]}\n{cd["phone"]}\n{cd['massage']}"
            send_mail(cd['subject'], messge, 'ashkan.spg@gmail.com')
            send = True

    else:
        form = TicketForm()
    return render(request, 'forms/ticket.html', {'form': form, 'send': send})


def post_list(request, tag_slug=None):
    posts = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
    context = {
        'posts': posts,
        'tag': tag,
    }
    return render(request, 'social/list.html', context=context)


def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('social:profile')
    else:
        form = CreatePostForm()
    return render(request, 'forms/creatpost.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_post = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_post = similar_post.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')[:2]

    context = {
        'post': post,
        'similar_post': similar_post

    }
    return render(request, "social/detail.html", context)
