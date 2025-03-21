from django.urls import path , include
from .views import AuthorizationsView
app_name = 'accounts'

urlpatterns = [
    path('api/v1/', include('accounts.api.v1.urls')),
    path('', AuthorizationsView.as_view(), name='authorizations'),
]
