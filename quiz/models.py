from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "General Knowledge"), (1, "Sport"), (2, "History"), (3, "Science & Nature"), (4, "Music & Media"), (5, "Past adventure"))

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_stamps", null=True)
    question = models.CharField(max_length=500, unique=True)
    answer = models.CharField(max_length=500, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.category} question by {self.user}"