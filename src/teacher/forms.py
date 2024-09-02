from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['gender', 'url_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }