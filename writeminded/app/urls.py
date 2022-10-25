from cgitb import html
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('ideanest', views.ideanest, name = 'ideanest'),
    path('sigin-signup', views.signinsignup, name = 'signinsignup'),
]

