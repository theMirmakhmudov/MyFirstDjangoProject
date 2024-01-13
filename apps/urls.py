from django.urls import path
from apps.views import main

urlpatterns = [
    path("web", main, name="main"),
]
