from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('signup/', views.signup, name='signup'),
   path('signin/', views.SignIn, name='signin'),
]