from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=200, null=False)
    url = models.URLField(null=False, unique=True)
    create_date = models.DateTimeField(default=datetime.now(), null=False)
    is_read = models.BooleanField(default=False, null=False)
    like = models.BooleanField(null=True)
    last_show_date = models.DateTimeField(default=datetime.now(), null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
