from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from .models import User


# Create your views here.
def user_signup(request):
    form = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
    else:
        form = SignupForm()
    return form

def security_signup(request, usertype = False):
    # TODO Set is_security on user model to true
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            userobj = User.objects.get(email=form.cleaned_data['email'])
            userobj.is_security = bool(usertype)
            userobj.save()

            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form, "user_type":"security"})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})