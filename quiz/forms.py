from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from . models import CustomUserModel

"""
User registration form
"""
class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    forename = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    surname = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    birthdate = forms.DateField(
        required=True,
        help_text='Required. Enter your date of birth.',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = CustomUserModel
        fields = ("username", "email", "forename", "surname", "birthdate", "password1", "password2")

    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        #if age < 18:
        #    raise ValidationError("You must be at least 18 years old to register.")
        return birthdate

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["forename"]
        user.last_name = self.cleaned_data["surname"]
        user.birthdate = self.cleaned_data["birthdate"]
        if commit:
            user.save()
        return user