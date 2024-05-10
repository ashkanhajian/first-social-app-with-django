from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .form import LoginForm

app_name = 'social'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    path('logout', views.log_out, name="logout"),
    path('register/', views.register, name='register'),
    path('ticket', views.ticket, name='ticket'),
    path('account/edit/', views.edit_account, name='edit_account')

]
