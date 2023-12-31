from django.db import models


# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    description = models.TextField()
    color = models.CharField(max_length=30,default="white")

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)



