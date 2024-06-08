from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    release = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.author}"