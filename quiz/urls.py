from . import views
from django.urls import path
from quiz.views import my_quiz, HomePage

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]