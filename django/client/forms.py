from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Per dire che quando usiamo save() dobbiamo aggiornare il database degli utenti
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]