from rest_framework.serializers import ModelSerializer
 
from .models import User, SpottedOffer
 
class UserSerializer(ModelSerializer):
     
    class Meta:
        model = User
        fields = ['url', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user
    

class SpottedOfferSerializer(ModelSerializer):
    class Meta:
        model = SpottedOffer
        fields = '__all__'
     