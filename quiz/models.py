from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "General Knowledge"), (1, "Sport"), (2, "History"), (3, "Science & Nature"), (4, "Music & Media"), (5, "Past adventure"))

#Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_stamps", null=True)
    question = models.CharField(max_length=500, unique=True)
    answer = models.CharField(max_length=500, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.category} question by {self.user}"


OPTIONS = ((0, "A"), (1, "B"), (2, "C"), (3, "D"))

# Create your models here.
class Multiple_choice_trivia(models.Model):
    question = models.CharField(max_length=256, unique=True)
    option_a = models.CharField(max_length=100, unique=False)
    option_b = models.CharField(max_length=100, unique=False)
    option_c = models.CharField(max_length=100, unique=False)
    option_d = models.CharField(max_length=100, unique=False)
    answer = models.IntegerField(choices=OPTIONS, default=0)

    def __str__(self):
        return f"{self.question}"