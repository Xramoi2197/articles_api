from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, ArticleByTagDetailView

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/<slug:tag_name>/", ArticleByTagDetailView.as_view()),
]