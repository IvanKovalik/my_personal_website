from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from taggit.models import Tag

from .models import Article, Project
from .forms import ContactForm


class IndexPageView(TemplateView):
    template_name = 'index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-date_created')[:5]
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


class ContactPageView(CreateView):
    template_name = 'contact_page.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        return redirect('success-page')


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


class SuccessContactView(TemplateView):
    template_name = 'contact_complete.html'
