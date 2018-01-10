from django.contrib.auth.models import User

from rest_framework import serializers
from .models import HomeOwner, Renter, Property


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class HomeOwnerSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = HomeOwner
        fields = '__all__'


class RenterSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Renter
        fields = '__all__'


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
