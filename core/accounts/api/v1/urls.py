from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

app_name = "accounts-api-v1"

urlpatterns = [
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    path(
        "change-password/",
        views.ChangePasswordView.as_view(),
        name="change-password",
    ),
    # path('activation/confirm)
]
