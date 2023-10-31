from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import PostForm
from .models import BlogPost,Category
from bs4 import BeautifulSoup

from random import choice
from itertools import chain


def post(request,category_name,post_id):
    """dispalying a particular post entirely"""
    post = BlogPost.objects.get(id = post_id) 
    all_posts = BlogPost.objects.all().order_by("-date_added")
    recent_posts = all_posts[:3]
    

    context = {"post":post,"recent_posts":recent_posts}
    return render(request,"core/post.html",context)


def category(request,category_name):
    """posts from a specific category"""
    category = Category.objects.get(name=category_name)
    posts = category.blogpost_set.order_by('-date_added')

    context = {"posts":posts,"category":category}
    return render(request,"core/category.html",context) 


def index(request):
    """The index page displaying the different posts"""
    all_posts = BlogPost.objects.all().order_by("-date_added")
    recent_posts = all_posts[:3]
    all_posts = list(all_posts)
    random.shuffle(all_posts)
    head_posts = all_posts[:2]
    all_main_posts = [x for x in all_posts if(x not in list(recent_posts) and list(head_posts))]
    main_posts = all_main_posts[:2]
    long_head_post = choice(all_main_posts)

    context = {"all_posts":all_posts,"recent_posts":recent_posts,"head_posts":head_posts,"main_posts":main_posts, "long_head_post":long_head_post}
    return render(request,"core/index.html",context)


def register(request):
    """register the user"""
    
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            user = User.objects.create(username=username,email=email,password=password1)
            user.save()

            #authenticated_user = authenticate(username=username,password=password1)
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse("core:index"))
        else:
            messages.info(request,"Passwords don't match")
            return HttpResponseRedirect(reverse("core:register"))

    return render(request,"core/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("core:index"))


def login_view(request):
    """login the user"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        #if user_auth is not None:
        #   login(request,user_auth)
        #  return HttpResponseRedirect(reverse("core:index"))
        

        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse("core:index"))

        else:
            messages.info(request,"invalid informations")
            return HttpResponseRedirect(reverse("core:login"))
    else:
        return render(request,"core/login.html")      

    


def add_post(request):
    """adding a post"""

    if request.method != "POST":
        """generate empty form"""
        form = PostForm()
    else:    
        """process data"""
        category_name = request.POST['category']
        category = Category.objects.get(name=category_name)
        cover_image = request.FILES.get('cover_image')
        form = PostForm(data=request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.category = category
            new_form.cover_image = cover_image

            new_form.save()
            return HttpResponseRedirect(reverse("core:index"))

    context={"form":form}        
    return render(request,"core/add_post.html",context)


def edit_post(request,post_id):
        """edit an existing post"""
        post = BlogPost.objects.get(id = post_id)
        if request.method != "POST":
            """generate pre-filled form"""
            form = PostForm(instance = post)

        else:
            """process and change the data"""
            form = PostForm(data=request.method,instance=post)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("core:index"))

        context = {"form":form}
        return render(request,"core/edit_post.html",context)

        return render(request,"core/edit_post.html")    