from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from .views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index-page'),
    path('work/', WorkPageView.as_view(), name='work-page'),
    path('projects/', ProjectsPageView.as_view(), name='projects-page'),
    path('articles/', ArticlesPageView.as_view(), name='articles-page'),
    path('cv/', ContactPageView.as_view(), name='contact-page'),

    path('articles/<slug:tag>/', ArticlesByTagPageView.as_view(), name='articles-python-page'),
    path('articles/by-id/<int:article_id>/', SomeArticleView.as_view(), name='some_article_page'),

    path('projects/by-id/<int:project_id>/', SomeProjectView.as_view()),

    path('work/by-id/<int:work_id>/', WorkProjectView.as_view()),
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
