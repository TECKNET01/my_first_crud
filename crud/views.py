from django.shortcuts import render,redirect
from django.contrib import auth


def login_view(request):
    return render(request,'crud/login.html')


def home_view(request):
    return render(request,'crud/home.html')

