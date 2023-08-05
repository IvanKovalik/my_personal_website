from django.db import models
from taggit.managers import TaggableManager


class Article(models.Model):
    name = models.CharField(max_length=1000, unique=True, blank=False)
    text = models.TextField(max_length=10000, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class Project(models.Model):
    preview_image = models.ImageField('Preview image')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    techs = models.CharField(max_length=100)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class WorkProject(models.Model):
    preview_image = models.ImageField('Preview image')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    techs = models.CharField(max_length=100)
    has_recommend_letter = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.name
