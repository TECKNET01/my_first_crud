from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import loginForm

@login_required(login_url = '/auth/login')
def login_view(request):
    form = loginForm()
    return render(request,'crud/login.html',{'form':form})


def home_view(request):
    return render(request,'crud/home.html')

