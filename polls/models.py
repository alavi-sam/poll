from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Question(models.Model):
    text = models.TextField(null=True)

    # Generic relation for question types
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Question: {self.text}"

class QuestionType(models.Model):
    # This model represents different question types
    
    question_type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Question Type: {self.question_type}"

class MultipleChoiceQuestion(models.Model):
    # Fields specific to multiple-choice questions
    question = GenericRelation(Question)
    # question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='multiple_choice_question', null=True)
    options = models.TextField()  # Store options as a JSON array or use another appropriate format

    def __str__(self):
        return f"MultipleChoiceQuestion: {self.options}"

class TextQuestion(models.Model):
    # Fields specific to text-based questions
    question = GenericRelation(Question)
    # question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='text_question', null=True)
    max_length = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"TextQuestion: Max Length - {self.max_length}"
