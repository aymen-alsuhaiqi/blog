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

@login_required
def add_comments(request,p_id):
    post = Post.objects.get(id=p_id)
    user = request.user
    if request.method == 'POST':
        comment = request.POST['comment']        
        new_comment = Comment.objects.create(post=post,user=user,comment=comment)
        new_comment.save()
        return redirect('/posts/'+str(p_id))
    else:
        pass
    return redirect('index')

def post_details(request,p_id):
    post = Post.objects.get(id=p_id)
    comments = Comment.objects.filter(post=post)
    return render(request,'posts/details.html',{'post':post,'comments':comments})