import os
import random
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    birthday = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    profile_image = forms.ImageField(required=False)

    # To say that when we use save() we need to update the user database
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'profile_image', 'password1', 'password2')

    # To override the save method to handle setting a default profile image if one is not provided
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)

        if 'profile_image' in self.cleaned_data and self.cleaned_data['profile_image']:
            user.profile_image = self.cleaned_data['profile_image']
        else:
            # Set a default profile image from static folder
            default_images_path = os.path.join(settings.STATIC_ROOT, 'images')
            default_images = [os.path.join(default_images_path, f) for f in os.listdir(default_images_path) if os.path.isfile(os.path.join(default_images_path, f))]
            if default_images:
                random_default_image = random.choice(default_images)
                user.profile_image = random_default_image[len(settings.STATIC_ROOT) + len('/images/'):]  # Storing path relative to STATIC_ROOT

        if commit:
            user.save()
        return user
