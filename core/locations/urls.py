from django.urls import path , include
from . import views

app_name = 'locations'

urlpatterns = [
    
    path('api/v1/', include('locations.api.v1.urls')),
]
