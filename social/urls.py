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
    path('account/edit/', views.edit_account, name='edit_account'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url='done'), name="password_change"),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(success_url='done'), name='password_rest'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(success_url='complete'),
         name='password_reset_confirm'),
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('posts/', views.post_list, name="post_list"),
    path('posts/tag/<slug:tag_slug>/', views.post_list, name="post_list_by_tag"),
    path('posts/create_post/', views.create_post, name='create_post'),
    path('post/detail/<pk>', views.post_detail, name='post_detail'),
    path('posts/<post_id>/comment', views.post_comment, name="post_comment"),
    path('like_post', views.like_post, name='like_post'),
    path('save-post/', views.save_post, name='save_post'),
    path('users/', views.user_list, name='user_list'),
    path('users/detail/', views.user_detail, name='user_list')
]

