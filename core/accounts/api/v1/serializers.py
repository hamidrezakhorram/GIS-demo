from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import User , Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer for user login using JWT
    """
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        
        validated_data["phone_number"] = self.user.phone_number
        validated_data["id"] = self.user.id
        return validated_data
    
class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    """
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["phone_number", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError(
                {"detail": "password does not match"}
            )

        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return User.objects.create_user(**validated_data)

class ChangepasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        def validate(self, attrs):
            if attrs.get("password") != attrs.get("password1"):
                raise serializers.ValidationError(
                    {"detail": "password does not match"}
                )

            try:
                validate_password(attrs.get("password"))
            except exceptions.ValidationError as e:
                raise serializers.ValidationError(
                    {"password": list(e.messages)}
                )

        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source="user.phone_number", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "phone_number", "first_name", "last_name"]
