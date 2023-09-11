from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Article(models.Model):
    name = models.CharField(max_length=1000, unique=True, blank=False)
    text = models.TextField(max_length=15000, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    minute_read = models.PositiveIntegerField()

    tags = TaggableManager()

    def __str__(self):
        return self.name


def get_upload_path():
    path = f'../media/project_images'
    return path


class Project(models.Model):
    preview_image = models.ImageField('Preview image', upload_to='project_images')
    name = models.CharField(max_length=100)
    # slug = models.SlugField(default=slugify(name))
    description = models.TextField(max_length=500)
    text = models.TextField(max_length=15000)
    what_have_been_done_by_me = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class WorkProject(models.Model):
    preview_image = models.ImageField('Preview image')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    text = models.TextField(max_length=15000)
    what_have_been_done_by_me1 = models.CharField(max_length=100)
    what_have_been_done_by_me2 = models.CharField(max_length=100, null=True)
    what_have_been_done_by_me3 = models.CharField(max_length=100, null=True)
    what_have_been_done_by_me4 = models.CharField(max_length=100, null=True)
    has_recommend_letter = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=300, blank=False)
    email = models.EmailField(max_length=300, blank=False)
    subject = models.CharField(max_length=500, blank=False)
    message = models.TextField(max_length=3000, blank=False)

    def __str__(self):
        return self.name
