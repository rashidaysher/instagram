from django import template
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import *
from .forms import PostForm, BioForm
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    template = loader.get_template('insta/index.html')

    if request.user.is_anonymous:
        context = {}
        return HttpResponse(template.render(context, request))

    posts = Post.objects.all()
    bios = Bio.objects.get(user=request.user)
    comments = Comment.objects.all()
    context = {'posts': posts, 'profile': bios, 'comments': comments}
    return HttpResponse(template.render(context, request))

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("user logged in ")
    else:
        return HttpResponse("user not logged in ")


def signup(request):
    pass


