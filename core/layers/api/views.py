from rest_framework import viewsets
from layers.models import Layer
from layers.api.serializers import LayerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LayerViewSet(viewsets.ModelViewSet):
    """
    API views using ViewSet for the Layer model
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
