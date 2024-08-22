from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Offense, Note, Student
from .forms import OffenseForm
from django.shortcuts import get_object_or_404

from django.shortcuts import redirect
from functools import wraps

def security_redirect(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_security:
            return redirect('statement_form')  # replace with your redirect URL or view name
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Create your views here.
@login_required
def statement(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        matric = request.POST.get('matric')  
        department = request.POST.get('department')  
        level = request.POST.get('level')
        statement = request.POST.get('offense') 


        new_student, _ = Student.objects.get_or_create(name=name, matric_no=matric, level=level, department=department)
        offenseObj = Offense.objects.create(student=new_student, statement=statement)
        offenseObj.status = Offense.Status.REPORT_WRITTEN
        offenseObj.save()

    # print(context['data'])
    return render(request, 'statement.html')

@login_required
def senate_offense(request, offense_id):
  print("GOT HERE ")
  offense = get_object_or_404(Offense, pk=offense_id)
  
  if request.method == 'POST':

    if 'set_under_investigation' in request.POST:
        content = request.POST.get('note')  # Get content from the request
        if content:  # Check if content is provided
            Note.objects.create(offense=offense, author=request.user, content=content)
            offense.status = Offense.Status.UNDER_INVESTIGATION
            offense.save()
        return redirect('home')  # Redirect to current update page
    
    postData = request.POST  # Get content from the request
    if postData.get("note"):
        Note.objects.create(offense=offense, author=request.user, content=postData.get("note"))
    if postData.get("conclusion"):
       offense.conclusion = postData.get("conclusion")

    offense.status = Offense.Status.RESOLVED
    offense.save()

    return redirect('home')  # Update success.html with your template name
  else:
    form = OffenseForm(instance=offense)

  return render(request, 'senate_offense.html', {'form': form, 'offense': offense})

@login_required
def sdc_offense(request, offense_id):
  print("GOT HERE ")
  offense = get_object_or_404(Offense, pk=offense_id)
  
  if request.method == 'POST':
    postData = request.POST  # Get content from the request
    if postData.get("note"):
      Note.objects.create(offense=offense, author=request.user, content=postData.get("note"))

    offense.recommendation = postData.get("recommendation")
    offense.status = Offense.Status.RECOMMENDATION
    offense.save()

    return redirect('home')  # Update success.html with your template name
  else:
    form = OffenseForm(instance=offense)

  return render(request, 'sdc_offense.html', {'form': form, 'offense': offense})

@login_required
@security_redirect
def home(request):
    resolved_offenses = None
    if request.user.is_sdc:
       offenses = Offense.objects.select_related('student').filter(status=Offense.Status.UNDER_INVESTIGATION)
    elif request.user.is_senate:
       offenses = Offense.objects.select_related('student').filter(status__in=(Offense.Status.REPORT_WRITTEN, Offense.Status.RECOMMENDATION,))
       resolved_offenses = Offense.objects.select_related('student').filter(status=Offense.Status.RESOLVED)
    elif request.user.is_superuser:
       offenses = Offense.objects.select_related('student').all()

    context = {
        "data": offenses,
        "resolved_offenses": resolved_offenses
        }
    # print(context['data'])
    return render(request, 'home.html', context)
