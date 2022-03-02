from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import quesmodel


class registration_form(UserCreationForm):
    username = forms.CharField(max_length=20, required=True,
                               widget=forms.TextInput(attrs={"placeholder": "Enter usernsme"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter email"}))
    password1 = forms.CharField(max_length=20, required=True,
                                widget=forms.PasswordInput(attrs={"placeholder": "Re-enter password"}))
    password2 = forms.CharField(max_length=20, required=True,
                                widget=forms.PasswordInput(attrs={"placeholder": "Re-enter password"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class login_form(forms.Form):
    login_email = forms.EmailField(required=True,
                                   widget=forms.EmailInput(attrs={'placeholder': 'email@gmail.com'}))
    login_password = forms.CharField(max_length=20, required=True,
                                     widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}))


class addquesform(forms.ModelForm):
    class Meta:
        model = quesmodel
        fields = ["question","answer"]


