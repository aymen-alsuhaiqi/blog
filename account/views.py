from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from post.models import Post
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # messages.success(request,'تم تسجيل الدخول بنجاح')
            return redirect('profile')
        else:
            messages.error(request,'خطأ باسم المستخدم او كلمة المرور')
            return render(request, 'accounts/login.html')

    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    # messages.success(request,'تم تسجيل الخروج')
    return redirect('login')

def profile(request):
    user_profile = None
    if request.user.is_authenticated:
        post = Post.objects.all().filter(author=request.user)
        if UserProfile.objects.filter(user=request.user).exists():
            user_profile = UserProfile.objects.get(user=request.user)
    else:
        messages.warning(request,'يجب تسجيل الدخول أولا')
        return redirect('login')
    return render(request, 'accounts/profile.html',{'user_profile':user_profile})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request,'accounts/signup.html')