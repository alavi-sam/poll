# Generated by Django 4.2.1 on 2023-11-16 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_choice_value_answer_text_value_choice_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='is_text',
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.choice'),
        ),
    ]
