from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_quiz(request):
    return HttpResponse("Lets build a great, fun, quiz app!")