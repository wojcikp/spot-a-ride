from rest_framework.serializers import ModelSerializer
 
from .models import User, Offer
 
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
    

class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
     