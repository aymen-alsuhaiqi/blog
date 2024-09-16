from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from post.models import Post
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'تم تسجيل الدخول بنجاح')
        else:
            messages.error(request,'خطأ باسم المستخدم او كلمة المرور')
            return render(request, 'accounts/login.html')

    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    post = None
    if request.user.is_authenticated:
        post = Post.objects.all().filter(author=request.user)
        print("__⚠️⚠️⚠️__ ~ file: views.py:27 ~ post:", post)
    else:
        messages.warning(request,'يجب تسجيل الدخول أولا')
        return redirect('login')
    return render(request, 'accounts/profile.html',{'post':post})