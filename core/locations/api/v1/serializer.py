from rest_framework import serializers
from locations.models import Points


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model and Points base on ModelSerializer
    """

    class Meta:
        model = Points
        fields = [
            "id",
            "user_id",
            "name",
            "code",
            "geom",
            "point_type",
            "created_at",
            "updated_at",
            "custom_fields",
            "image_name",
            "image",
            "audio",
            "video",
        ]

    def validate_custom_fields(self, value):
        """
        Validate the custom_fields to ensure it is a dictionary
        and contains key-value pairs with valid types.
        """
        if not isinstance(value, dict):
            raise serializers.ValidationError(
                "Custom fields must be a dictionary."
            )
        for key, field in value.items():
            if not isinstance(key, str):
                raise serializers.ValidationError(
                    "Custom field keys must be strings."
                )
            if not isinstance(field, (int, float, str, bool, list, dict)):
                raise serializers.ValidationError(
                    f"Invalid type for custom field '{key}'. Must be one of: int, float, str, bool, list, dict."
                )
        return value
