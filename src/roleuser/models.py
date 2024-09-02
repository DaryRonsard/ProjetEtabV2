from django.db import models

# Create your models here.
class RoleUser(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)