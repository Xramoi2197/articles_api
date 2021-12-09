from rest_framework import serializers
from .models import Article, Tag
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    tags = serializers.SlugRelatedField(
        slug_field="tag_name", queryset=Tag.objects.all(), many=True
    )

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
