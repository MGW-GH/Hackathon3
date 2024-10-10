from . import views
from django.urls import path
#from django.contrib.auth import views as auth_views
from quiz.views import QuizPage, HomePage, ScoresPage, UserRegistrationView, UserSuccessView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    # Scores Page
    path('scores/', ScoresPage.as_view(), name='scores'),
    # Account related urls
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("registration/success/", UserSuccessView.as_view(), name="user_registration_success"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]