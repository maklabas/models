from datetime import date
from django.db import models
from teachers.models import Teacher


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start = models.DateField(blank=True, default=date.today)
    end = models.DateField(blank=True, default=date.today)

    def __str__(self):
        return self.name
