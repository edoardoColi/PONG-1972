from django.urls import path, include
from .views import deafultPage

urlpatterns = [
    path('', deafultPage),
]