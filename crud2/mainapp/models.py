# from platform import mac_ver
from email.policy import default
from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll = models.IntegerField(blank=False)
    Address = models.CharField(max_length=100)
    Pincode = models.IntegerField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

