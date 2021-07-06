from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=14, blank=False)
    date_of_birth = models.DateField(blank=False)
    FK = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
