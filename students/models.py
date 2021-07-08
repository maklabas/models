from django.db import models

from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(blank=False, max_length=25)
    facebook = models.URLField(blank=True)
    date_of_birth = models.DateField(blank=False)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
