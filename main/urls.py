from django.urls import path
from . import views

urlpatterns = [
        path("", views.shorturl, name="shorturl"), 
]
