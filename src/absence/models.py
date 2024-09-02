from django.db import models
from student.models import Student
from teacher.models import Teacher

# Create your models here.
class Absence(models.Model):
    absence_date = models.DateField()
    absence_number = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='student_address', null=True, blank=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='teacher_address', null=True, blank=True)

    def __str__(self):
        return f"Absence on {self.absence_date} for {self.student}"