from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=300)

class ProductStock(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to="static/img/products")
