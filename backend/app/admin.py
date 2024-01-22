from django.contrib import admin
from .models import User, Offer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass