from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from Post_app.models import Video
from accounts.forms import UserForm


def connection(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,"Bienvenue")
            return redirect("home")
        else:
            messages.error(request,"Erreur d'authentification")
    return  render(request,"accounts/login.html")

@login_required(login_url="login")
def profile_completed(request):
    user=request.user
    return render(request,"accounts/profile_register.html")
def register(request):
    form=UserForm()
    if request.method=='POST':
        type=request.POST.get('type')
        print(type)
        form=UserForm(data=request.POST)
        if form.is_valid():
            #form.type=type
            form.save()
            messages.success(request,'Votre compte a été créé')
            return redirect('login')
        else:
            messages.error(request,form.errors)
    return  render(request,"accounts/register.html",context={"form":form})

@login_required(login_url='login')
def deconnection(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def profile(request):
    post_videos=Video.objects.filter(user=request.user)
    context={'user':request.user,"post_videos":post_videos}
    return render(request,"pages/profile.html",context)