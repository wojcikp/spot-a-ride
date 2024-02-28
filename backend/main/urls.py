from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
 
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'spotted-offers', views.SpottedOfferViewSet, basename='SpottedOffer')
router.register(r'searched-offers', views.SearchedOfferViewSet, basename='SearchedOffer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('user-id/', views.UserId.as_view(), name='user_id'),
    path('scrap-for-new-search/', views.ScrapOffersForNewSearch.as_view(), name='scrap_for_new_search'),
]
