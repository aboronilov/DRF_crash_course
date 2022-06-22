from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import api_home

urlpatterns = [
    path('', api_home),
    path('auth/', obtain_auth_token),
]