from rest_framework import serializers
from locations.models import Location

class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model and Points base on ModelSerializer
    """
    class Meta:
        model=Location
        fields = ['id', 'name', 'code','geom','point_type' , 'created_at','updated_at', 'image_name','image']

