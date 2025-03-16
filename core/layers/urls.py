from django.urls import path , include

app_name = 'layers'

urlpatterns = [
    path('api/', include('layers.api.urls')),
]
