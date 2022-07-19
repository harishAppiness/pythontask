# from platform import mac_ver
from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll = models.IntegerField(blank=False)
    Address = models.CharField(max_length=100)
    Pincode = models.IntegerField()

    def __str__(self):
        return self.Name

