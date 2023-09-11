from .models import Article, Project, WorkProject
from django.contrib import admin

from taggit.models import TaggedItem

admin.site.register(Project)
admin.site.register(WorkProject)
admin.site.register(TaggedItem)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'text']
