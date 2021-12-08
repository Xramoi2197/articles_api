from django.contrib import admin

from .models import Tag, Article

# Register your models here.
class TagsInline(admin.StackedInline):
    model = Article.tags.through
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title", "url"]
    list_display = (
        "id",
        "title",
        "url",
        "user",
        "create_date",
        "last_show_date",
        "is_read",
        "like",
    )
    list_filter = ["tags", "create_date"]
    inlines = [TagsInline]
    exclude = ("tags",)


admin.site.register(Article, ArticleAdmin)
