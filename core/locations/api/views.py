from rest_framework import viewsets
from locations.models import Location
from locations.api.serializer import LocationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LocationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Location model and Points
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

