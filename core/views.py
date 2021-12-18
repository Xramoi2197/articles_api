from rest_framework import generics, viewsets, pagination, filters

from .serializers import ArticleSerializer, TagSerializer
from .models import Article, Tag

# Pagination classes
class ArticlePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class TagPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    ordering = "tag_name"
    max_page_size = 50


# ViewSets classes
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
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

    def get_queryset(self):
        queryset = Article.objects.all().order_by("create_date")
        tag_name = self.request.query_params.get("tag")
        if tag_name is not None:
            try:
                tag = Tag.objects.get(tag_name=tag_name.lower())
                queryset = queryset.filter(tags=tag)
            except:
                queryset = queryset.none()
        return queryset


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = TagPagination
    search_fields = ["tag_name"]
    filter_backends = [
        filters.SearchFilter,
    ]
