from django.db import models
from django.contrib.auth.models import AbstractUser
 
class User(AbstractUser):
    pass


class Offer(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    url = models.CharField()
    date_spotted = models.DateTimeField(auto_now_add=True)
    date_disappeared = models.DateTimeField(blank=True)
    brand = models.CharField()
    model = models.CharField()
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.IntegerField()
