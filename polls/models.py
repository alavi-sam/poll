from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from accounts.models import User
from django.utils import timezone
# Create your models here.


class Survey(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='surveys')
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class QuestionType(models.Model):
    question_type = models.CharField(max_length=100)

    def __str__(self):
        return self.question_type


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    question_type = models.ForeignKey(QuestionType, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question= models.ForeignKey(Question, models.CASCADE, related_name='choices')
    is_text = models.BooleanField(default=False)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"for question: {self.question_id}, added choice: {self.value}"
    

class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_time = models.DateTimeField(auto_now_add=True)

    @property
    def question_type(self):
        return self.question.question_type
    
    def __str__(self):
        return f"user {self.user.first_name + ' ' + self.user.last_name},\
          answered question {self.question.title} with {self.choice.value} choice."


class Test(models.Model):
    pass