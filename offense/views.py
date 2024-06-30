from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Offense
import json 

# Create your views here.
@login_required
def statement(request):
    context = {
        # "data": serializers.serialize("json", Offense.objects.all().values()),
        "data": (list(Offense.objects.all().values()))
    }
    # print(context['data'])
    return render(request, 'form.html', context)

def home(request):
    context = {
        # "data": serializers.serialize("json", Offense.objects.all().values()),
        "data": (list(Offense.objects.all().values()))
    }
    # print(context['data'])
    return render(request, 'home.html', context)