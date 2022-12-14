from cgitb import html
from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('ideanest', views.ideanest, name = 'ideanest'),
    path('listoffilesIN', views.listoffilesIN, name = 'listoffilesIN'),
    path('uploadfileIN', views.uploadfileIN, name = 'uploadfileIN'),
    path('viewfileIN', views.viewfileIN, name = 'viewfileIN'),
    path('addideaIN', views.addideaIN, name = 'addideaIN'),
    path('groupfilesIN', views.groupfilesIN, name = 'groupfilesIN'),
    path('showgroupIN', views.showgroupIN, name = 'showgroupIN'),
]

