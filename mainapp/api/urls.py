from django.urls import path

from .views import TestAPIView
from .views import UserAPIView

urlpatterns = [
    path('productsData/', TestAPIView.as_view(), name='productsData'),
    path('Data/', UserAPIView.as_view(), name='Data')
]