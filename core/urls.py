from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, TagViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="articles")
router.register("tags", TagViewSet, basename="tags")

urlpatterns = [
    path("", include(router.urls)),
]
