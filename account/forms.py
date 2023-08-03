from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from new_app.models import Product


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'photo')