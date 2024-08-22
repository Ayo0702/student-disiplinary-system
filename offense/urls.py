from django.urls import path
from . import views

urlpatterns = [
 path('senate/update/<int:offense_id>/', views.senate_offense, name='senate_offense'),
 path('statementform/', views.statement, name='statement_form'),
 path('sdc/update/<int:offense_id>/', views.sdc_offense, name='sdc_offense'),
 path('home/', views.home, name='home'),
]