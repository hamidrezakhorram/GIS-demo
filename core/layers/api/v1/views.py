from rest_framework import viewsets
from layers.models import Layer
from .serializers import LayerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class LayerViewSet(viewsets.ModelViewSet):
    """
    API views using ViewSet for the Layer model
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_fields = ['layer_type']
    search_fields = ['name']
    ordering_fields = ['uploaded_at']




