# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField
from taggit.managers import TaggableManager


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name='date of brith', null=True, blank=True)
    bio = models.TextField(verbose_name="bio", null=True, blank=True)
    photo = models.ImageField(verbose_name="user photo", upload_to='account_images/', blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name='jon title', null=True, blank=True)
    phone = models.CharField(max_length=11)


class Post(models.Model):
    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts", verbose_name="نویسنده")
    # data fields

    description = models.TextField(verbose_name="توضیحات")

    # date

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    # choice fields

    # reading_time = models.PositiveIntegerField(verbose_name="زمان مطالعه")

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.author.first_name
