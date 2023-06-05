from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from.import views
def index(request):
   
    return render(request,'index.html')
# Create your views here.
