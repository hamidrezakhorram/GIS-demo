from django.urls import path , include
from . import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='locations'),
    path('api/', include('locations.api.urls')),
]
