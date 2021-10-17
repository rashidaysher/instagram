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


def user_bio(request, username):
    template = loader.get_template('insta/bio.html')
    bio = Bio.objects.get(user=request.user)
    posts = Post.objects.filter(author__user__username=request.user.username)
    context = {'bio': bio, 'posts': posts}
    return HttpResponse(template.render(context, request))

def top_comment(request):
    if request.POST:
        description, id = request.POST['description'], request.POST['demo']
        post = Post.objects.get(pk=id)
        if description is not None:
            Comment.objects.create(post_linked=post, description=description, user=request.user)
            return redirect(reverse('index'))

def likes_post(request, postid):
    post = Post.objects.get(id=postid)
    try:
        is_Liked = Likes.objects.get(post_linked=post, user__username=request.user.username)
        Likes.objects.filter(post_linked=post, user__username=request.user.username).delete()
        post.likes -= 1
    except Likes.DoesNotExist:

        Likes.objects.create(post_linked=post, user=request.user)
        post.likes += 1
    post.save()
    return redirect(reverse('index'))


def add_post(request):
    template = loader.get_template('insta/post.html')
    profile = Bio.objects.get(user=request.user)
    if request.method == "POST":
        bio = Bio.objects.get(user=request.user)
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = bio
            fs.save()
            return redirect(reverse('index'))
    else:
        form = PostForm()
        pass

    context = {'form': form ,'bio':bio}
    return HttpResponse(template.render(context, request))

