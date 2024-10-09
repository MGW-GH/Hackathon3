from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
#from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from . forms import UserRegistration


# Create your views here.
class QuizPage(TemplateView):
    """
    Displays quiz page
    """
    template_name = 'base.html'


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'base.html'


class UserRegistration(CreateView):
    """
    Displays user registration page
    """
    form_class = UserRegistration
    success_url = ("login")
    template_name = "accounts/registration/registration-user.html"