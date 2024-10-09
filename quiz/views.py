from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, LoginView, LogoutView

from . forms import UserRegistrationForm, UserLoginForm


# Create your views here.
class QuizPage(TemplateView):
    """
    Displays quiz page
    """
    template_name = 'quiz.html'


class HomePage(TemplateView):
    """
    Displays home page
    """
    #template_name = 'base.html'
    template_name = 'index.html'


class ScoresPage(TemplateView):
    """
    Displays scores page
    """
    template_name = 'scores.html'


class UserRegistrationView(CreateView):
    """
    Displays user registration page and handles user registration
    """
    form_class = UserRegistrationForm
    template_name = "accounts/registration/registration-user.html"