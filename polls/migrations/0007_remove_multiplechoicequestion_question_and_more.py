# Generated by Django 4.2.1 on 2023-11-13 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoicequestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='textquestion',
            name='question',
        ),
    ]
