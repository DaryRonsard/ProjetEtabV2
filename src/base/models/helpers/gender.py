from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class GenderModel(models.TextChoices):
    MALE = "H", _("Homme")
    FEMALE = "F", _("Femme")
    OTHER = "O", _("Autre")