from rest_framework import viewsets
from locations.models import Location
from locations.api.serializer import LocationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from locations.api.paginations import LocationPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter


class LocationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Location model and Points
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = LocationPagination
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_fields = ['point_type']
    search_fields = ['name']
    ordering_fields = ['created_at']


