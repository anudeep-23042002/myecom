from ast import mod
from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from itertools import product
from pyexpat import model
from statistics import quantiles
from unicodedata import category, name
from django.db import models

# Create your models here.
class Item(models.Model):
    name =  models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField(default="h")
    category=models.TextField(default="other")
    discount=models.IntegerField(default=0)
    discount_price=models.IntegerField(default=0);
    price=models.IntegerField(default=0)
    more_description=models.TextField(default="")
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.TextField(default="other")
    def __str__(self):
        return self.name;
class Cart(models.Model):
    user=models.IntegerField(default=0)
    product=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
class Orders(models.Model):
    user=models.IntegerField(default=0)
    address=models.TextField(default="")
    city=models.TextField(default="")
    state=models.TextField(default="")
    zip=models.TextField(default="")
    pro=models.TextField(default="")
    sum=models.IntegerField(default=0)
    status=models.TextField(default="ordered")
    estimated_date=models.DateField(default=datetime.now)
