from django.db import models
from student.models import Student
# Create your models here.


class StudentCard(models.Model):
    reference = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='card')