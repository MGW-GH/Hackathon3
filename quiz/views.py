from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class QuizPage(TemplateView):
    """
    Displays quiz page"
    """
    template_name = 'quiz.html'


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'base.html'
