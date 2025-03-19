from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer





class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        
        validated_data["phone_number"] = self.user.phone_number
        validated_data["id"] = self.user.id
        return validated_data