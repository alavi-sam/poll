from django.db import models
from accounts.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType



# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    author = models.OneToOneField(User, on_delete=models.SET_NULL())
    creation_date = models.DateTimeField(default=timezone.now())



class Question(models.Model):
    pass


class Subjective(models.Model):
    pass


class MultipleChoice(models.Model):
    pass


class DropDown(models.Model):
    pass


class StarRating(models.Model):
    pass


