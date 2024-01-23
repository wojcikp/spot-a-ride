from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from .serializers import UserSerializer, SpottedOfferSerializer
from .permissions import UserPermission, IsOwnerOrReadOnly
from .models import User, SpottedOffer
 
class UserViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')


class SpottedOfferViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = SpottedOfferSerializer
    queryset = SpottedOffer.objects.all()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hi there!'}
        return Response(content)
