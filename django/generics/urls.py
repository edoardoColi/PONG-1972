from django.urls import path, re_path, include
from . import views

# Resolution order from top to bottom
urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('', include("django.contrib.auth.urls")),      # inluding this it has inside all the resolver for: login/ logout/  password_change/  password_reset/ ...

    path('', views.home_page, name="home"),
    path('user/<str:name>/', views.profile_page, name="profile"),
    path('games/', views.games_page, name="games"),

    # Define a catch-all URL pattern using a regular expression
    re_path(r'^.*$', views.error_page, name="error"),
]
