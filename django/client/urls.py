from django.urls import path, include
from . import views, forms

# Resolution order from top to bottom
urlpatterns = [
    path('', views.redirect_to_account, name="redirect_to_account"),    # defines URL pattern but also assigns the name "redirect_to_account" to it, allowing you to reference this URL pattern by name in your Django application, such as in templates or in Python code using the {% url %} template tag or the reverse() function
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='client/login.html', authentication_form=forms.LoginForm), name='login'),
    path('logout/',views.loggovia),
    path('', include("django.contrib.auth.urls")),      # inluding this it has inside all the resolver for: login/ logout/  password_change/  password_reset/ ...
    path('<str:name>/', views.user_page),
]
