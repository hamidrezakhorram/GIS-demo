from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('points',views.LocationViewSet,basename='points')
app_name ='locations-api'
urlpatterns = router.urls
urlpatterns += [
    
]
