from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    return render(request,'register.html')


def signin(request):
    return render(request,'login.html')


def sign_out(request):
    logout(request)
    return redirect('index')