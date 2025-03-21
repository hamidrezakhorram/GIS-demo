from rest_framework import serializers
from layers.models import Layer

class LayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Layer model
    """
    class Meta:
        model = Layer
        fields = ['id', 'name', 'layer_type', 'file', 'uploaded_at', 'label_enabled']

