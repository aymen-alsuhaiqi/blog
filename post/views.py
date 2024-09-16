from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'pages/index.html',{'posts':posts})

@login_required
def add_post(request):
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            print(form.errors)
        form = AddPostForm()
    return render(request,'posts/add.html',{'form':form})