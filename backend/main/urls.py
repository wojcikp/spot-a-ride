from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
 
from app.views import UserViewSet, SpottedOfferViewSet, SearchedOfferViewSet
from app import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'spotted-offers', SpottedOfferViewSet)
router.register(r'searched-offers', SearchedOfferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
