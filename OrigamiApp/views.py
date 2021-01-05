from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from OrigamiApp.forms import UserSignUp, UserProfileSignUp
from OrigamiApp.models import UserProfile, UserBlog
from django.contrib.auth.models import User
from django.db.models import Model

# Create your views here.

def index(request):
    return render(request, 'index.html')

def history(request):
    return render(request, 'history.html')

def application(request):
    return render(request, 'application.html')

def method(request):
    return render(request, 'method.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        error = ''
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'User not active!'
        else:
            error = 'Username or password incorrect'
        
        return render(request, 'signin.html', {'error': error,
                                                'username': username})

    return render(request, 'signin.html')
          
def signup(request):
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        profile_form = UserProfileSignUp(request.POST)

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if form.is_valid() and profile_form.is_valid():
            if len(password) < 8:
                return render(request, 'signUp.html', {'error': 'Password must be longer than 8 characters!',
                                                        'username': username,
                                                        'email': email,
                                                        'first_name': first_name,
                                                        'last_name': last_name, })
    
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
        
        elif str(form.errors).find('exists') > -1:
            return render(request, 'signUp.html', {'error': 'A user with that username already exists!',
                                                    'username': username,
                                                    'email': email,
                                                    'first_name': first_name,
                                                    'last_name': last_name, })
    
        return HttpResponseRedirect('/signin')

    return render(request, 'signUp.html')

def blog(request):
    return render(request, 'sample_blog.html')
