from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Multiple_choice_trivia
from django.contrib.auth.views import LoginView, LogoutView


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
    template_name = 'base.html'
    # template_name = 'index.html'


class UserRegistrationView(CreateView):
    """
    Displays user registration page and handles user registration
    """
    form_class = UserRegistrationForm
    template_name = "accounts/registration/registration-user.html"
    success_url = reverse_lazy('user_registration_success')
    

class UserSuccessView(TemplateView):
    """
    Displays user registration success page
    """
    template_name = "accounts/registration/registration-success.html"

class UserLoginView(LoginView):
    """
    Displays login page
    """
    form_class = UserLoginForm
    template_name = 'accounts/login-user.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

# logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')