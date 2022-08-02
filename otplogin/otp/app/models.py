from django.db import models

# Create your models here.
class UserInfo(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=30)
    otp = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email