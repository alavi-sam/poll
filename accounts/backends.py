from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest


class LoginBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        UserModel = get_user_model()
        if username is None:
            pass
