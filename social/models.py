
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name='date of brith', null=True, blank=True)
    bio = models.TextField(verbose_name="bio", null=True, blank=True)
    photo = models.ImageField(verbose_name="user photo", upload_to='account_images/', blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name='jon title', null=True, blank=True)
    phone = models.CharField(max_length=11)
