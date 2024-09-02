from django.db import models
from base.models.helpers.person import Person
from student.models import Student
from teacher.models import Teacher
# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='address', null=True, blank=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='address', null=True, blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"