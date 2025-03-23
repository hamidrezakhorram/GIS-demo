from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("layers", views.LayerViewSet, basename="layers")
app_name = "layers-api"
urlpatterns = router.urls
urlpatterns += []
