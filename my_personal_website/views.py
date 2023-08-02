from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index_page.html'


class WorkPageView(TemplateView):
    template_name = 'work_page.html'


class ProjectsPageView(TemplateView):
    template_name = 'projects_page.html'


class ArticlesPageView(TemplateView):
    template_name = 'articles_page.html'


class ContactPageView(TemplateView):
    template_name = 'contact_page.html'


class CreateArticlePage(TemplateView):
    template_name = 'create_article.html'
