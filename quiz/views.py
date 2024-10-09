from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Multiple_choice_trivia
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.http import JsonResponse


from . forms import UserRegistrationForm, UserLoginForm


def QuizPage(request):
    if request.method == 'POST':
        questions = Multiple_choice_trivia.objects.filter(question__in=request.POST.getlist('question_id'))
        score = 0

        for question in questions:
            selected_answer = request.POST.get(f'q-{question.question}')
            if selected_answer == 'A':
                selected_answer = 0
            if selected_answer == 'B':
                selected_answer = 1
            if selected_answer == 'C':
                selected_answer = 2
            if selected_answer == 'D':
                selected_answer = 3

            if selected_answer == question.answer:
                score += 1
        
        message = get_score_message(score)
        
        return JsonResponse({'score': score, 'message': message})

    else:
        questions = Multiple_choice_trivia.objects.all().order_by('?')[:5]
        return render(request, 'quiz.html', {'questions': questions})


def get_score_message(score):
    if score == 5:
        return "Perfect score! Excellent job!"
    elif score == 4:
        return "Great job! Almost perfect!"
    elif score == 3:
        return "Good effort! You're on the right track."
    elif score == 2:
        return "Not bad, but there's room for improvement."
    else:
        return "Keep practicing, you'll get better!"
    
    return render(request, 'quiz.html', context)


class HomePage(TemplateView):
    """
    Displays home page
    """
    # template_name = 'base.html'
    template_name = 'index.html'


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