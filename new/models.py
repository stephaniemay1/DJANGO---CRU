from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    image = models.ImageField(upload_to='images/', blank=False, default="default.jpg")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=40, blank=False)
    phone = models.IntegerField(blank=False)
    subject = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


