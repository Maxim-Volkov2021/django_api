from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        max_length=200,
        unique=True
    )

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    tags = models.ManyToManyField(Tags)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True
    )
    timeCreate = models.DateTimeField(auto_now_add=True)
    timeUpdate = models.DateTimeField(auto_now=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


