from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def ideanest(request):
    return render(request, "ideanest.html")

def listoffilesIN(request):
    return render(request, "listoffilesIN.html")

def uploadfileIN(request):
    return render(request, "uploadfileIN.html")

def viewfileIN(request):
    return render(request, "viewfileIN.html")

def addideaIN(request):
    return render(request, "addideaIN.html")

def groupfilesIN(request):
    return render(request, "groupfilesIN.html")

def showgroupIN(request):
    return render(request, "showgroupIN.html")