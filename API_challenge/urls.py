from .api import status, repair_bay, teapot
from django.urls import path

urlpatterns = [
    path('status/', status, name = "status"),
    path('repair-bay/', repair_bay, name = "repair_bay"),
    path('teapot/', teapot, name = "teapot")
]