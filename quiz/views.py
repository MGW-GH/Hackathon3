from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Multiple_choice_trivia

from . forms import UserRegistrationForm, UserLoginForm

# Create your views here.
# class QuizPage(TemplateView):
#     """
#     Displays quiz page
#     """
#     template_name = 'quiz.html'
 

# def QuizPage(request):
    
#     questions = Multiple_choice_trivia.objects.all()
#     context = {'products':products, 'cartItems':cartItems}
    
#     return render(request, 'quiz/templates/quiz.html', context)

def QuizPage(request):
    print("Im here and I'm being called")
    questions = Multiple_choice_trivia.objects.all().order_by('?')[:5]  # Get 5 random questions
    context = {'questions': questions}
    
    return render(request, 'quiz.html', context)


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