from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def ideanest(request):
    return render(request, "ideanest.html")

def signinsignup(request):
    return render(request, "signin-signup.html")