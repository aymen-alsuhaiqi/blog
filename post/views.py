from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'pages/index.html',{'posts':posts})