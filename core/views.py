from rest_framework import generics, viewsets, pagination, filters

from .serializers import ArticleSerializer, TagSerializer
from .models import Article, Tag

# Pagination classes
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


# ViewSets classes
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = ArticlePagination
    ordering_fields = [
        "create_date",
        "last_show_date",
    ]
    search_fields = [
        "title",
        "url",
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = TagPagination
    search_fields = ["tag_name"]
    filter_backends = [
        filters.SearchFilter,
    ]


# ListView classes
class ArticleByTagDetailView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"].lower()
        tag = Tag.objects.get(tag_name=tag_name)
        return Article.objects.filter(tags=tag)
