from django.db import models

# Create your models here.
class Course(models.Model):
    pname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    mdesc=models.CharField(max_length=500)
    mprice=models.FloatField()

class Trainers(models.Model):
    tname=models.CharField(max_length=50)
    ttechnology=models.CharField(max_length=200)
    texperience=models.CharField(max_length=200)

class Testimonials(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=60)
    comment=models.CharField(max_length=500)
