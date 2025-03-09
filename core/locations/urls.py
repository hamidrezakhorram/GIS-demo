from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocationsView.as_view(), name='locations'),
]
