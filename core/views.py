from rest_framework import generics, viewsets, pagination

from .serializers import ArticleSerializer, TagSerializer
from .models import Article, Tag


class ArticlePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    ordering = "create_date"
    max_page_size = 50


class TagPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    ordering = "tag_name"
    max_page_size = 50


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = ArticlePagination


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = TagPagination


class ArticleByTagDetailView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"].lower()
        tag = Tag.objects.get(tag_name=tag_name)
        return Article.objects.filter(tags=tag)
