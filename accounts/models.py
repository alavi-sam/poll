from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

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
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        self.create_user(username, password, email, phone_number, **extra_fields)

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    creation_date = models.DateTimeField(_("creation date"), blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number', 'password']

    objects = CustomUserManager()

    def save(self):
        if not self.pk:
            self.creation_date = timezone.now()
        super().save()
