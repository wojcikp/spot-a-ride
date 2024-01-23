from django.contrib import admin
from .models import User, SpottedOffer, SearchedOffer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(SpottedOffer)
class SpottedOfferAdmin(admin.ModelAdmin):
    pass


@admin.register(SearchedOffer)
class SearchedOfferAdmin(admin.ModelAdmin):
    pass