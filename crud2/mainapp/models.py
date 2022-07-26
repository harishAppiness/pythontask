# from platform import mac_ver
from audioop import maxpp
from email.policy import default
from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll = models.CharField(max_length=100, blank=True)
    Address = models.CharField(max_length=100)
    Pincode = models.IntegerField()
    email = models.CharField(max_length=100, blank=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name


class TotalCountStudent(models.Model):
    count = models.PositiveIntegerField(default=0)
    total_counts = models.PositiveIntegerField(default=0,blank=True, null=True)

    def __int__(self):
        return self.count


