from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from accounts.models import User
from django.utils import timezone
# Create your models here.


class BaseQuestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=200)


class MultipleChoiceQuestion(models.Model):
    question_id = models.ForeignKey(BaseQuestion, on_delete=models.CASCADE)
