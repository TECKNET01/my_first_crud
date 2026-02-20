from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse

def home_view(request):
    return render(request,'crud/home.html')
