from django.db import models

# Create your models here.
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone_no = models.CharField(max_length=12,blank=True)

    def __str__(self):
        return self.username



class Restaurant(models.Model):
    RestaurantNmame = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=12)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.RestaurantNmame

class Item(models.Model):
    ItemName = models.CharField(max_length=100)

    def __str__(self):
        return self.ItemName
    
class Menu(models.Model):
    RestaurantName = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    ItemName = models.ForeignKey(Item,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

class Order(models.Model):
    username = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100,default=None)
    price = models.IntegerField()
    phoneno = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username