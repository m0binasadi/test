from .views import site 
from django.urls import path

app_name = "app"

urlpatterns = [
    path('',site)
]
