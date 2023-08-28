from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index-page'),
    path('work/', WorkPageView.as_view(), name='work-page'),
    path('projects/', ProjectsPageView.as_view(), name='projects-page'),
    path('articles/', ArticlesPageView.as_view(), name='articles-page'),
    path('contact/', ContactPageView.as_view(), name='contact-page'),

    path('articles/<slug:tag>/', ArticlesByTagPageView.as_view(), name='articles-python-page'),

    path('articles/by-id/<int:article_id>/', SomeArticleView.as_view(), name='some_article_page'),

    path('contact/success/', SuccessContactView.as_view(), name='success-page'),
]
