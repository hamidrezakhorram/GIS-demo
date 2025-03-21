from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import generics , status
from .serializers import RegistrationSerializer
from rest_framework.response import Response

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View for user login using JWT
    """
    serializer_class = CustomTokenObtainPairSerializer

class RegistrationView(generics.GenericAPIView):
    """
    View for user registration
    """
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"phone_number": serializer.validated_data["phone_number"]}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)