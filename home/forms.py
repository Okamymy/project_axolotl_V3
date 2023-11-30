from django import forms
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Ingrese su username"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"type":"password", "class":"form-control", "placeholder":"Ingrese su password"}))

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu user"}))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Escribe tu password"}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"confirma tu password"}))
    first_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu first name"}))
    last_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu last name"}))
    email = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu email"}))

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email"
        ]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"