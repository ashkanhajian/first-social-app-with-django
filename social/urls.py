from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .form import LoginForm
app_name = 'social'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(authentication_form=LoginForm), name="login"),
    path('logout', views.log_out, name="logout"),

]