from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from .serializers import UserSerializer
from .permissions import UserPermission
from .models import User
 
class UserViewSet(ModelViewSet):
    permission_classes = [UserPermission, IsAuthenticated,]

    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-date_joined")

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hi there!'}
        return Response(content)
