from rest_framework.serializers import ModelSerializer
 
from .models import User, SpottedOffer, SearchedOffer
 
class UserSerializer(ModelSerializer):
     
    class Meta:
        model = User
        fields = ['url', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            user = User(username=validated_data['username'], email=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return user
    

class SpottedOfferSerializer(ModelSerializer):
    class Meta:
        model = SpottedOffer
        fields = '__all__'


class SearchedOfferSerializer(ModelSerializer):
    class Meta:
        model = SearchedOffer
        fields = '__all__'
     