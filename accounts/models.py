from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager):
    def create_user(self, username, password, email, phone_number, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not phone_number:
            raise ValueError(_("The phone number must be set"))
        email = self.normalize_email(email)
        user = self.model(username=username, phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, email, phone_number, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not phone_number:
            raise ValueError(_("The phone number must be set"))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    USERNAME_FIELD = 'username'