from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Patients(models.Model):
    PatientId = models.AutoField(primary_key=True)
    PatientName = models.CharField(max_length=500)
    PatientImg = models.CharField(max_length=500)
    Con_Doc    = models.CharField(max_length=500)
    Diagnosis  = models.CharField(max_length=500)


class Doctors(AbstractUser):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500,unique=True)
    password=models.CharField(max_length=500)
    phone = models.CharField(max_length=500,default="0000000000")
    address = models.CharField(max_length=500,default="0000000000")
    specification = models.CharField(max_length=500,default="0000000000")
    isadmin = models.BooleanField(default=False)
    isvalid = models.CharField(max_length=500,default="waiting")
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    