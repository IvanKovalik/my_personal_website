from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from taggit.models import Tag

from .models import Article, Project


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


class ArticlesByTagView(TemplateView):
    template_name = 'article_by_tag_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['tags'] = Tag.objects.all()
        context['articles'] = Article.objects.filter(tags=context['tag'])
        return context


def get_articles(request, tag):
    tags = Tag.objects.all()
    articles = Article.objects.filter(tags=tag)
    context = {
        'articles': articles,
        'tags': tags,
    }
    return render(request, 'article_by_tag_page.html', context=context)


def get_some_article(request, article_id, tag):
    tags = Tag.objects.all()
    article = Article.objects.filter(tags=tag, id=article_id)
    context = {
        'tags': tags,
        'article': article,
    }
    return render(request, 'some_project_page.html', context=context)
