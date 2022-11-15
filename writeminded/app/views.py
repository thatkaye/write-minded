from .models import uploadfilemodel
from app.forms import uploadfileform # for upload file
import subprocess
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def uploadfileIN(request):
    if request.method == 'POST':
        form = uploadfileform(request.POST, request.FILES)

        for f in request.FILES.getlist('file'):
            print(str(f))

        file = request.FILES.getlist('file')[0]
        fileModel = uploadfilemodel.objects.create(file = file)
        fileModel.save()
        messages.info(request, "file has been uploaded")
        # return HttpResponse("the name of uploaded file is " + str(fileModel.file))
    else:
        form = uploadfileform()
    
    return render(request, "uploadfileIN.html", {'form': form})

def home(request):
    return render(request, "home.html")

def ideanest(request):
    return render(request, "ideanest.html")

def listoffilesIN(request):
    return render(request, "listoffilesIN.html")

def viewfileIN(request):
    return render(request, "viewfileIN.html")

def addideaIN(request):
    return render(request, "addideaIN.html")

def groupfilesIN(request):
    return render(request, "groupfilesIN.html")

def showgroupIN(request):
    return render(request, "showgroupIN.html")