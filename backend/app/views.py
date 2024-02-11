from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from .serializers import UserSerializer, SpottedOfferSerializer, SearchedOfferSerializer
from .permissions import UserPermission, IsOwnerOrReadOnly
from .models import User, SpottedOffer, SearchedOffer
 
class UserViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')


class SpottedOfferViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = SpottedOfferSerializer

    def get_queryset(self):
        return SpottedOffer.objects.filter(user=self.request.user)


class SearchedOfferViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = SearchedOfferSerializer
    queryset = SearchedOffer.objects.all()


class UserId(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return(Response({'userId': request.user.id}))

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hi there!'}
        return Response(content)
