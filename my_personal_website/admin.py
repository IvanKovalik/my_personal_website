from .models import Article, Project, WorkProject, Contact
from django.contrib import admin

admin.site.register(Project)
admin.site.register(WorkProject)
admin.site.register(Contact)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'text']
