from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print("Got 'ere")
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})
