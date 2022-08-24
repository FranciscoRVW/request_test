# request_test/urls.py
from django.urls import path
from .views import apiV1

urlpatterns = [
    path("api/v1/envelope/", apiV1)
]