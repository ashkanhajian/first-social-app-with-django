from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'bio', 'phone']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'photo', 'job', 'bio', 'phone')}),
    )


def make_deactivation(modeladmin, request, queryset):
    result = queryset.update(active=True)
    modeladmin.message_user(request, f"{result}post was deleted")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'created', 'description']
    ordering = ['created']
    search_fields = ['description']
    inlines = [ImageInline, CommentInline]
    actions = [make_deactivation]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'title', 'created']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'created']
    list_filter = ['created']
    search_fields = ['name', 'body']
    # list_editable = ['active']


admin.site.register(Contact)
