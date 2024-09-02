from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Utilisation du bon modèle
from django import forms


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
