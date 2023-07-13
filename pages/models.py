from django.db import models

# Create your models here.

class Team(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    insta = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    createdate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.firstname
