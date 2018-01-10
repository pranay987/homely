from rest_framework import viewsets

from .models import HomeOwner, Renter, Property
from .serializers import HomeOwnerSerializer
from .serializers import RenterSerializer
from .serializers import PropertySerializer

# Create your views here.
class HomeOwnerViewSet(viewsets.ModelViewSet):
    queryset = HomeOwner.objects.all()
    serializer_class = HomeOwnerSerializer


class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
