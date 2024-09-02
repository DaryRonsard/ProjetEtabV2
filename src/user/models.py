from django.contrib.auth.models import AbstractUser
from django.db import models

from roleuser.models import RoleUser


class User(AbstractUser):
    creation_date = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(RoleUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
