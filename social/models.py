# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField
from django.urls import reverse
from django_resized import ResizedImageField
from taggit.managers import TaggableManager


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name='date of brith', null=True, blank=True)
    bio = models.TextField(verbose_name="bio", null=True, blank=True)
    photo = models.ImageField(verbose_name="user photo", upload_to='account_images/', blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name='jon title', null=True, blank=True)
    phone = models.CharField(max_length=11)
    following = models.ManyToManyField('self', through='Contact', related_name='followers', symmetrical=False)

    # def get_absolute_url(self):
    #     return reverse('social:user_detail', args=[self.username])


class Post(models.Model):
    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts", verbose_name="نویسنده")
    # data fields

    description = models.TextField(verbose_name="توضیحات")

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    total_likes = models.PositiveIntegerField(default=0)
    saved_by = models.ManyToManyField(User, related_name='saved_posts')

    # choice fields

    # reading_time = models.PositiveIntegerField(verbose_name="زمان مطالعه")

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes'])

        ]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.author.first_name

    def get_absolute_url(self):
        return reverse('social:post_detail', args=[self.id])

    def delete(self, *args, **kwargs):
        for img in self.images.all():
            storage, path = img.image_file.storage, img.image_file.path
            storage.delete(path)
        super().delete(*args, **kwargs)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images", verbose_name="post")
    image_file = ResizedImageField(upload_to="post_images/", quality=100)

    title = models.CharField(max_length=250, verbose_name="title", null=True, blank=True)
    description = models.TextField(verbose_name="description", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="post")
    name = models.CharField(max_length=250, verbose_name="username")
    body = models.TextField(verbose_name="comment")
    created = models.DateTimeField(auto_now_add=True, verbose_name="created time")


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['-created_at'])]
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.user_from}follows{self.user_to}'
