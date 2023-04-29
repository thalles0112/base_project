from django.db import models

# Create your models here.


class DefaultModel(models.Model):
    defaultField = models.CharField(max_length=100)