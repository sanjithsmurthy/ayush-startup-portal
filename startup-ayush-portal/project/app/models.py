from django.db import models
from django.contrib.postgres.fields import JSONField

class Animation(models.Model):
    name = models.CharField(max_length=255)
    data = JSONField()