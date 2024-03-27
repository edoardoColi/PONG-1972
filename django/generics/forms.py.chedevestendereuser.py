from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Insert a valid email address.')
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    birthday = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    # To say that when we use save() we need to update the user database
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2')
