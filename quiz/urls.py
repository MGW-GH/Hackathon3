from . import views
from django.urls import path
from quiz.views import QuizPage, HomePage, UserRegistration

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    # Registration Page
    path("UserRegistration/", UserRegistration.as_view(), name="UserRegistration"),

]