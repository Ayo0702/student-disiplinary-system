from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms 
from .models import User

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': "form-control",           'placeholder':'', }),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': "form-control",           'placeholder':'', }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class SignupForm(CustomUserCreationForm):

    class Meta:
        model = User 
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder':'',  
                'class': "form-control",
                }),
            'last_name': forms.TextInput(attrs={
                'placeholder':'', 
                'class': "form-control",
                }),
            'email': forms.EmailInput(attrs={
                'placeholder':'', 
                'class': "form-control", 
                })
        }

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'', 'class': 'form-control'}))