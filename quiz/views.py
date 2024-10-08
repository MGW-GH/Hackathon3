from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def my_quiz(request):
    return HttpResponse("Lets build a great, fun, quiz app!")


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'
