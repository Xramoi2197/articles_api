from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    @action(detail=True)
    def change_json(self, request, pk=None):
        data = Article.objects.all()
        serializer = ArticleSerializer(instance=data, many=True)
        print(serializer.data)
        return Response(None)
