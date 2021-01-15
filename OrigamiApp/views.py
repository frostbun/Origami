from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings

from . import forms
from OrigamiApp.forms import UserSignUp, UserProfileSignUp, UploadBlog, UploadCmt
from OrigamiApp.models import UserProfile, UserBlog, Comment
from django.contrib.auth.models import User
from django.db.models import Model

# Create your views here.

def index(request):
    return render(request, 'index.html')

# @login_required    
def lichsu(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

        cmt_form = UploadCmt(request.POST)
        if cmt_form.is_valid():
            cmt = cmt_form.save(commit=False)
            cmt.trang = "lichsu"
            cmt.user = request.user
            cmt.save()
        return HttpResponseRedirect(request.path)

    post_cmt = Comment.objects.filter(trang = "lichsu").order_by('date').reverse
    user_profile = UserProfile.objects.get(user = request.user)
    return render(request, 'lichsu.html', {'post_cmt': post_cmt,
                                            'form':UploadCmt,
                                            'user_profile': user_profile} )

@login_required
def kythuat(request):
    if request.method == 'POST':
        cmt_form = UploadCmt(request.POST)
        if cmt_form.is_valid():
            cmt = cmt_form.save(commit=False)
            cmt.trang = "kythuat"
            cmt.user = request.user
            cmt.save()
        return HttpResponseRedirect(request.path)

    post_cmt = Comment.objects.filter(trang = "kythuat").order_by('date').reverse

    return render(request, 'lichsu.html', {'post_cmt': post_cmt,
                                            'form':UploadCmt})

@login_required
def phanloai(request):
    if request.method == 'POST':
        cmt_form = UploadCmt(request.POST)
        if cmt_form.is_valid():
            cmt = cmt_form.save(commit=False)
            cmt.trang = "phanloai"
            cmt.user = request.user
            cmt.save()
        return HttpResponseRedirect(request.path)

    post_cmt = Comment.objects.filter(trang = "phanloai").order_by('date').reverse

    return render(request, 'lichsu.html', {'post_cmt': post_cmt,
                                            'form':UploadCmt})

@login_required
def ungdung(request):
    if request.method == 'POST':
        cmt_form = UploadCmt(request.POST)
        if cmt_form.is_valid():
            cmt = cmt_form.save(commit=False)
            cmt.trang = "ungdung"
            cmt.user = request.user
            cmt.save()
        return HttpResponseRedirect(request.path)

    post_cmt = Comment.objects.filter(trang = "ungdung").order_by('date').reverse

    return render(request, 'lichsu.html', {'post_cmt': post_cmt,
                                            'form':UploadCmt})

def docthem(request):
    return render(request, 'docthem.html')

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

@login_required
def profile(request):
    if request.method == 'POST':
        blog_form = UploadBlog(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user
            blog.save()

        profile_form = UserProfileSignUp(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = UserProfile.objects.get(user = request.user)
            profile.pic = profile_form.cleaned_data['pic']
            profile.save()

        return HttpResponseRedirect(request.path)

    all_blog = UserBlog.objects.filter(user = request.user).order_by('date_posted').reverse
    user_profile = UserProfile.objects.get(user = request.user)
    return render(request, 'profile.html', {'all_blog': all_blog,
                                            'form': UploadBlog,
                                            'user_profile': user_profile} )
