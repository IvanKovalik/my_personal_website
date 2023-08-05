from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Tag, Article, Project


class IndexPageView(TemplateView):
    template_name = 'index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class WorkPageView(TemplateView):
    template_name = 'work_page.html'


class ProjectsPageView(TemplateView):
    template_name = 'projects_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['articles'] = Article.objects.all()
        context['projects'] = Project.objects.all()
        return context


class ArticlesPageView(TemplateView):
    template_name = 'articles_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['articles'] = Article.objects.all()
        return context


class ContactPageView(TemplateView):
    template_name = 'contact_page.html'
