from django.db import models


# Create your models here.

class Projectmodel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    url = models.URLField()

class ExperienceModel(models.Model):
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
