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

    def get_queryset(self):
        return SearchedOffer.objects.filter(user=self.request.user)


class UserId(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return(Response({'userId': request.user.id}))
    

class ScrapOffersForNewSearch(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        from .scrappers import scrapper_job_for_new_offer

        new_offers = scrapper_job_for_new_offer(
            request.user,
            request.query_params.get('searched_offer_id'),
            request.query_params.get('brand'),
            request.query_params.get('model'),
            request.query_params.get('production_year_from'),
            request.query_params.get('production_year_to'),
            request.query_params.get('mileage_limit'),
            request.query_params.get('price_limit')
        )
        spotted_offers = SpottedOfferSerializer(new_offers, many=True)

        return Response(spotted_offers.data)
