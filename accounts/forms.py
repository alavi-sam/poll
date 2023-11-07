from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.db import transaction

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.lower()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use!')
        return email.lower()

    def clean_username(self):
        username = self.cleaned_data['username']
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use!')
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        User = get_user_model()
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('This phone number is already in use!')
        return phone_number

    @transaction.atomic
    def save(self, commit=True):
        User = get_user_model()
        user_instance = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            password=self.cleaned_data['password2'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user_instance
