from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    url_logo = models.CharField(max_length=255, null=True, blank=True)