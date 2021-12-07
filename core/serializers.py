from rest_framework import serializers
from .models import Article, Tag
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="user", queryset=User.objects.All())
    tags = serializers.SlugRelatedField(slug_field="tags", queryset=Tag.objects.All())

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "url",
            "create_date",
            "is_read",
            "like",
            "last_show_date",
            "user",
            "tags",
        )
