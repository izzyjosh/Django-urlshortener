from django.urls import path
from . import views

urlpatterns = [
        path("", views.shorturl, name="shorturl"), 
        path("<str:str>/", views.main_url, name="main")
]
