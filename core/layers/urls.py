from django.urls import path, include

app_name = "layers"

urlpatterns = [
    path("api/v1/", include("layers.api.v1.urls")),
]
