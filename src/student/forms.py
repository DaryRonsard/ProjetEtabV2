from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['gender', 'url_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }