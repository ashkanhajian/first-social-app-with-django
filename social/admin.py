from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'bio', 'last name']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'photo', 'job', 'bio')}),
    )
