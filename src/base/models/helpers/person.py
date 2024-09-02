from django.db import models
from .gender import GenderModel
from django.contrib.auth.models import AbstractUser


class Person(models.Model):


    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    alt_phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderModel.choices, default=GenderModel.MALE, verbose_name="Genre")
    url_picture = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True