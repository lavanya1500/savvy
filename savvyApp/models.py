from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=200)

class LogIn(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)

class Complaints(models.Model):
    selectcategory=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    landmark=models.CharField(max_length=200)
    photo = models.ImageField(upload_to="complaint_photos/images", default="")
