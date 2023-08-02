from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=1000, unique=True, blank=False)
    # author =
    text = models.TextField(max_length=10000, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
