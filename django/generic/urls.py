from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('games/', views.gamesPage),

    # Define a catch-all URL pattern using a regular expression
    re_path(r'^.*$', views.errorPage),
]
