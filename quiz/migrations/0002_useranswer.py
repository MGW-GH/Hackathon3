# Generated by Django 4.2.16 on 2024-10-10 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_answer', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')])),
                ('is_correct', models.BooleanField(default=False)),
                ('trivia_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.multiple_choice_trivia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
