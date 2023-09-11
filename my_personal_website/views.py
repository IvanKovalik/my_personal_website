from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from taggit.models import Tag

from .models import Article, Project, WorkProject


class IndexPageView(TemplateView):
    template_name = 'index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-date_created')[:5]
        context['tags'] = Tag.objects.all()
        return context


class WorkPageView(TemplateView):
    template_name = 'work_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_projects'] = WorkProject.objects.all().order_by('-date_created')
        return context


class WorkProjectView(CreateView):
    pass


class ProjectsPageView(TemplateView):
    template_name = 'projects_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['articles'] = Article.objects.all()
        context['projects'] = Project.objects.all().order_by('-time_created')
        return context


class SomeProjectView(CreateView):
    template_name = 'some_project_page.html'

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['project_id'])
        return render(request, self.template_name, {'project': project})


class ArticlesPageView(TemplateView):
    template_name = 'articles_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tags'] = Tag.objects.all()
        context['tags'] = Tag.objects.filter(taggit_taggeditem_items=5)
        context['articles'] = Article.objects.all()
        return context


class ContactPageView(CreateView):
    template_name = 'contact_page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ArticlesByTagView(TemplateView):
    template_name = 'article_by_tag_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['tags'] = Tag.objects.all()
        context['articles'] = Article.objects.filter(tags=context['tag'])
        return context


class ArticlesByTagPageView(CreateView):
    template_name = 'article_by_tag_page.html'

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        tag_id = Tag.objects.get(slug__exact=kwargs['tag'])

        articles = Article.objects.filter(tags=tag_id)
        context = {
            'articles': articles,
            'tags': tags,
        }
        return render(request, 'article_by_tag_page.html', context=context)


class SomeArticleView(CreateView):
    template_name = 'some_article_page.html'

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()

        article = Article.objects.get(id=kwargs['article_id'])
        context = {
            'tags': tags,
            'article': article,
        }
        return render(request, self.template_name, context=context)
