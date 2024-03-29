from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to='patients/profile_pictures', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to='doctors/profile_pictures', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
