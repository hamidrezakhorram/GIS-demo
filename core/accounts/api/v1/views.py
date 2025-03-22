from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer , ChangepasswordSerializer , ProfileSerializer
from rest_framework import generics , status
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import Profile
User = get_user_model()

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
    

class ChangePasswordView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangepasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(
                serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["wrong password"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        # queryset = self.get_queryset()
        # obj =get_object_or_404(queryset , user =queryset.request.user)
        # return obj
        if not self.request.user.is_authenticated:
            raise NotAuthenticated(detail="User is not authenticated.")
        return get_object_or_404(Profile, user=self.request.user)
