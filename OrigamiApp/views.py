from django.shortcuts import render
from OrigamiApp.forms import UserSignUp, UserProfileSignUp
from OrigamiApp.models import UserProfile, UserBlog
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        profile_form = UserProfileSignUp(request.POST)

        if form.is_valid() and profile_form.is_valid():
            error = ''
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if email.find('.') < email.find('@'):
                error = 'Please enter a valid email!'
            
            if len(password) < 8:
                error = 'Password must be longer than 8 characters!'

            if len(error):
                return render(request, 'signUp.html', {'error': error,
                                                       'username': username,
                                                       'email': email,
                                                       'firsr_name': first_name,
                                                       'last_name': last_name, })

            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.pic = request.FILES['pic']
            profile.save()


    return render(request, 'signUp.html')

def blog(request):
    return render(request, 'sample_blog.html')
