from rest_framework import serializers
from locations.models import Points

class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model and Points base on ModelSerializer
    """
    class Meta:
        model=Points
        fields = ['id', 'user_id', 'name', 'code','geom','point_type' , 'created_at','updated_at', 'image_name','image', 'audio', 'video']

