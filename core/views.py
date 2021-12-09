from rest_framework import viewsets, pagination

from .serializers import ArticleSerializer
from .models import Article


class ArticleViewPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    ordering = "create_date"
    max_page_size = 50


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = ArticleViewPagination
