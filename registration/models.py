from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
# Create your models here.

class Employee(AbstractUser):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=30,choices=GENDER)
    phone=models.IntegerField(null=True,blank=False)
    image=models.ImageField(upload_to='members')

class Patient(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female')
    )
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30,choices=GENDER)
    phone=models.IntegerField(null=True,blank=False)
    appointment_date=models.DateField()

    def __str__(self):
        return self.first_name
