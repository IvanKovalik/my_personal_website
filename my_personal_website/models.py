from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    # tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.tag_name


class Article(models.Model):
    name = models.CharField(max_length=1000, unique=True, blank=False)
    text = models.TextField(max_length=10000, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    preview_image = models.ImageField('Preview image')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    techs = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name