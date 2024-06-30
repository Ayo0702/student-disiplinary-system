from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.security_signup, name='register'),
    path('login/', views.user_login, name='login'),
]