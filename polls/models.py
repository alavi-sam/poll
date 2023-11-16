from django.db import models
from accounts.models import User
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
    # is_text = models.BooleanField(default=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_text(self):
        if self.question.question_type.question_type == 'text':
            return True
        return False

    def save(self, *args, **kwargs):
        if self.is_text:
            return None
        super(Choice, self).save(*args, **kwargs)

    def __str__(self):
        return f"for question: {self.question_id}, added choice: {self.value}"
    

class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='answers', on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text_value = models.TextField(null=True, blank=True)
    answer_time = models.DateTimeField(auto_now_add=True)

    @property
    def question_type(self):
        return self.question.question_type

    @property
    def is_text(self):
        if self.question.question_type.question_type == 'text':
            return True
        return False

    def save(self, *args, **kwargs):
        if not self.is_text:
            self.text_value = None
        else:
            self.choice = None
        super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        return f"user {self.user.first_name + ' ' + self.user.last_name},\
          answered question {self.question.title} with {self.choice.value} choice."


