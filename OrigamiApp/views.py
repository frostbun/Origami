from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def history(request):
    return render(request, 'history.html')

def application(request):
    return render(request, 'application.html')

def method(request):
    return render(request, 'method.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signUp.html')