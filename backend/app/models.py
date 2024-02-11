from django.db import models
from django.contrib.auth.models import AbstractUser
 
class User(AbstractUser):
    pass


class SpottedOffer(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    searched_offer = models.ForeignKey('SearchedOffer', on_delete=models.CASCADE)
    otomoto_url = models.CharField()
    date_spotted = models.DateTimeField(auto_now_add=True)
    date_disappeared = models.DateTimeField(blank=True, null=True)
    otomoto_id = models.CharField()
    otomoto_title = models.CharField()
    brand = models.CharField()
    model = models.CharField()
    img = models.CharField(blank=True, null=True)
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.IntegerField()


class SearchedOffer(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    brand = models.CharField()
    model = models.CharField(blank=True, null=True)
    production_year_from = models.IntegerField(blank=True, null=True)
    production_year_to = models.IntegerField(blank=True, null=True)
    mileage_limit = models.IntegerField(blank=True, null=True)
    price_limit = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        from .scrappers import scrapper_scheduled_job
        scrapper_scheduled_job()
        super(SearchedOffer, self).save(*args, **kwargs)
